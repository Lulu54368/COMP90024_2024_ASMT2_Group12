import requests
from mastodon import Mastodon, StreamListener
from bs4 import BeautifulSoup
from datetime import datetime
from zoneinfo import ZoneInfo
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
from scipy.special import expit
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import urllib3
import json

urllib3.disable_warnings()

# Connect to Elasticsearch using username and password
es_client = Elasticsearch(
    "https://127.0.0.1:9200/",
    #api_key = "b9c59b70-88fb-44d5-b00b-ba18f87a3970"
    verify_certs=False,
    basic_auth = ("elastic","elastic"))

# Mastodon Access Token and Base URL
MASTODON_ACCESS_TOKEN = "Q8oYzpl2vDz6-SOcyf2upfwpUiKS-K9N4qTVLyo2qfA"
MASTODON_BASE_URL = 'https://mastodon.au'

INDEX_NAME = 'mastodon'

# Initialize Mastodon API
m = Mastodon(api_base_url=MASTODON_BASE_URL, access_token=MASTODON_ACCESS_TOKEN)

# Sentiment Analysis and Text-to-Plain Converter
nltk.download('vader_lexicon', quiet=True)
sid = SentimentIntensityAnalyzer()

# Load Topic Classification Model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_path = "cardiffnlp/tweet-topic-21-multi"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path).to(device)
class_mapping = model.config.id2label


# Function for Processing Toots
def toot_processing(raw_toot):
    # Convert and Reformat DateTime to Australia/Sydney Timezone
    sydney_timezone = ZoneInfo("Australia/Sydney")
    sydney_datetime = raw_toot['created_at'].astimezone(sydney_timezone)
    created_at = sydney_datetime.strftime("%Y-%m-%d %H:%M:%S %Z")

    # Extract Text Content and Analyze Sentiment
    soup = BeautifulSoup(raw_toot['content'], 'html.parser')
    for link in soup.find_all('a'):
        link.replace_with(link.get_text())
    content = soup.get_text().replace("\n", " ").strip()
    sentiment_score = sid.polarity_scores(content)["compound"]

    tokens = tokenizer(content, return_tensors='pt', max_length=512, truncation=True).to(device)
    output = model(**tokens)
    scores = expit(output["logits"][0].detach().cpu().numpy())
    topics = [class_mapping[i] for i, prediction in enumerate((scores >= 0.5) * 1) if prediction]
    separator = '_&_'
    if isinstance(topics, list):
        topics = separator.join(topics)
        
    return {
        'id': raw_toot['id'],
        'created_at': created_at,
        'content': content,
        'sentiment_score': sentiment_score,
        "topics": topics,
        'url': raw_toot['url'],
        'language': raw_toot['language']
    }

# Listener Class for Streaming Toots
class Listener(StreamListener):
    def __init__(self, upper_limit):
        super().__init__()
        self.count = 0
        self.upper_limit = upper_limit

    def on_update(self, status):
        if status["language"] == "en":
            toot_processed = toot_processing(status)
            # print(toot_processed)
            response = es_client.index(index=INDEX_NAME, body=toot_processed)
            print(response)
            self.count += 1
            if self.count % 50 == 0:
                print(f"Has harvested {self.count} toots.")
            if self.count >= self.upper_limit:
                raise StopStreamingException("Stopping streaming.")


# Custom Exception to Stop Streaming
class StopStreamingException(Exception):
    pass
    
# Main Execution
if __name__ == '__main__':
    header = {"Authorization": f"Bearer {MASTODON_ACCESS_TOKEN}"}
    r = requests.get(f"{MASTODON_BASE_URL}/api/v1/accounts/verify_credentials", headers=header)
    print(r.json())
    listener = Listener(10000)
    try:
        m.stream_public(listener)
    except StopStreamingException as e:
        print(e)
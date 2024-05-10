import json

with open('./final.json', 'r') as json_file:
    json_data = json.load(json_file)

data = []

for tweet in json_data:
    for topic in tweet.get('topics', []):
        new_tweet = tweet.copy()
        new_tweet['topic'] = topic
        del new_tweet['topics']
        data.append(new_tweet)

with open('tweet.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
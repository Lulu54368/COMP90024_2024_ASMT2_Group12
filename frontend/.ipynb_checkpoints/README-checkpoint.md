API:

MASTODON
GET  /num/mastadon_toots

{
    "mastadon-total":800, int
}

GET  /num/mastadon_toots(sentiment between -1 to 0)

{
    "mastadon-total":800,   int
}

GET  /num/mastadon_toots(sentiment between 0 to 1)

{
    "mastadon-total":800,   int
}


POST /mastadon_toots
{'id': 112406071622032721,  int
'created_at': '2024-05-09 01:02:14 AEST', string
'content': 'Heardle Lyrical #405🔊🟩⬜️⬜️⬜️⬜️⬜️#Heardle #Lyrics #Music #HeardleDecades @heardledecadeshttps://lyrical.heardledecades.xyz/',   string
'sentiment_score': 0.0,    float
'topics': ['music'],   array
'url': 'https://mastodon.social/@BrownSquirrel/112406071515854940', String
'language': 'en'} String

GET /topic/mastadon_toots

{
    "topic":  ['music'],(only one topic) Array
    "num_of_toots_of_the_topic": 80 ,   int
}(filter non_english)


GET /sentiment/mastadon_toots (sentiment between -1 to 0)

{
    "topic":  ['music'],(only one topic)   array
    "num_of_toots_of_the_topic": 80 ,   int
}

GET /sentiment/mastadon_toots (sentiment between 0 to 1)

{
    "topic": ['music'] ,(only one topic) array
    "num_of_toots_of_the_topic":  80,  int
}

TWITTER

GET /sentiment/twitter_tweets(sentiment between -1 to 0)

{
    "topic": ['music'] ,(only one topic)
    "num_of_toots_of_the_topic":  80,
}

GET /sentiment/twitter_tweets(sentiment between 0 to 1)

{
    "topic": ['music'] ,(only one topic)
    "num_of_toots_of_the_topic":  80,
}

GET /num/twitter_tweets

{
    "tweeter-total":800,
}

GET  /num/twitter_tweets(sentiment between -1 to 0)

{
    "mastadon-total":800,
}

GET  /num/twitter_tweets(sentiment between 0 to 1)

{
    "mastadon-total":800,
}

GET /topic/twitter_tweets

{
    "topic": ['music'] ,(only one topic)
    "num_of_toots_of_the_topic": 80 ,
}

GET /region/sentiment

{
    "SA2_NAME21": "Beaumaris"
    "average_sentiment":0.415,
}


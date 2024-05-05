API:

MASTODON
GET  /num/mastadon_toots

{
    "mastadon-total":800,
}

GET  /num/mastadon_toots(sentiment between -1 to 0)

{
    "mastadon-total":800,
}
GET  /num/mastadon_toots(sentiment between 0 to 1)

{
    "mastadon-total":800,
}
POST /mastadon_toots

{
    'id': ,
    'created_at': ,
    'content': ,
    'sentiment_score': ,
    "topics": ,
    'url': ,
    'language': 
}
GET /topic/mastadon_toots

{
    "topic":  ,(only one topic)
    "num_of_toots_of_the_topic":  ,
}(filter non_english)



GET /sentiment/mastadon_toots (sentiment between -1 to 0)

{
    "topic":  ,(only one topic)
    "num_of_toots_of_the_topic":  ,
}
GET /sentiment/mastadon_toots (sentiment between 0 to 1)

{
    "topic":  ,(only one topic)
    "num_of_toots_of_the_topic":  ,
}

TWITTER
GET /sentiment/twitter_tweets(sentiment between -1 to 0)

{
    "topic":  ,(only one topic)
    "num_of_toots_of_the_topic":  ,
}
GET /sentiment/twitter_tweets(sentiment between 0 to 1)

{
    "topic":  ,(only one topic)
    "num_of_toots_of_the_topic":  ,
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
    "topic":  ,(only one topic)
    "num_of_toots_of_the_topic":  ,
}


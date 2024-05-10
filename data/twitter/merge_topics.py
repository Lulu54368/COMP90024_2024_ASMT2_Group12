import json

with open('./final.json', 'r') as json_file:
    json_data = json.load(json_file)

data = []

for tweet in json_data:
    separator = '_&_'
    if isinstance(tweet['topics'], list):
        tweet['topics'] = separator.join(tweet['topics'])
    data.append(tweet)

with open('tweet.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
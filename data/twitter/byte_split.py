import json
import os
import datetime
from mpi4py import MPI
from collections import Counter

begin_time = datetime.datetime.now()

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
output_dir = './geooutput'
geo_tweets = []  # List to store tweets with non-empty geo
batch_index = 0
batch_size = 10000
# File processing
total_bytes = os.path.getsize('./twitter-100gb.json')
begin = rank * total_bytes // size
end = begin + total_bytes // size
current = begin
def write_batch_to_file(batch, batch_index):
    filename = f'{output_dir}/geo_tweets_part{batch_index}.json'
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(batch, file)

with open('./twitter-100gb.json', 'r', encoding='utf-8') as tweet_file:
    tweet_file.seek(begin)
    tweet_file.readline()  # Skip to the first full line

    while (tweet_str := tweet_file.readline()) != '{}]}\n':
        if current > end:
            break

        tweet_data = json.loads(tweet_str[:-2])
        if tweet_data.get('doc', {}).get('data', {}).get('geo', {}):  # Check if geo is not empty
            geo_tweets.append(tweet_data)
            if len(geo_tweets) >= batch_size:
                write_batch_to_file(geo_tweets, batch_index)
                geo_tweets= []
                batch_index += 1

        current += len(tweet_str.encode('utf-8'))

# Gather and merge results
geo_tweets_result = comm.gather(geo_tweets, root=0)

if rank == 0:

    finish_time = datetime.datetime.now()
    print('Total processing time: ', finish_time - begin_time)
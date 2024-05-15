from flask import request, current_app
import requests, logging
import json
from collections import defaultdict
def config(k):
    with open(f'/configs/default/shared-data/{k}', 'r') as f:
        return f.read()

def config_twitter(k):
    with open(f'/configs/default/twitter-data/{k}', 'r') as f:
        return f.read()
def main():
    current_app.logger.info(f'Received request: ${request.headers}')
    r = requests.get(config_twitter('TWITTER_URL'),
        verify=False,
        auth=(config('ES_USERNAME'), config('ES_PASSWORD')),
        json= json.loads(config_twitter('TWITTER_REQ_BODY_GT')))
    buckets = r.json()['aggregations']["split_values"]['buckets']
    aggregated_data = defaultdict(int)
    # Modify the "key" values using map and lambda
    for bucket in buckets:
        bucket['key'] = bucket['key'].strip('_')
        aggregated_data[bucket['key']] += bucket['doc_count']
    aggregated_data = dict(aggregated_data)
    
    current_app.logger.info(f'Status ES request: {r.status_code}')
    return aggregated_data
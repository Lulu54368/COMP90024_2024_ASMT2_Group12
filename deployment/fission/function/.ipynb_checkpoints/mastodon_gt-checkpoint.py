# Team 12
# Meilun Yao   1076213
# Yingyi Luan 1179002
# Yuntao Lu 1166487
# Jiayi Xu 1165986
# Zheyuan Wu 1166034
from flask import request, current_app
import requests, logging
import json
from collections import defaultdict
def config(k):
    with open(f'/configs/default/shared-data/{k}', 'r') as f:
        return f.read()

def config_mastodon(k):
    with open(f'/configs/default/mastodon-data/{k}', 'r') as f:
        return f.read()
def main():
    current_app.logger.info(f'Received request: ${request.headers}')
    r = requests.get(config_mastodon('MASTODON_URL'),
        verify=False,
        auth=(config('ES_USERNAME'), config('ES_PASSWORD')),
        json= json.loads(config_mastodon('MASTODON_REQ_BODY_GT')))
    response = r.json()["aggregations"]
    buckets = response["topics_count"]['buckets']
    aggregated_data = defaultdict(int)
    # Modify the "key" values using map and lambda
    for bucket in buckets:
        bucket['key'] = bucket['key'].strip('_')
        aggregated_data[bucket['key']] += bucket['doc_count']
        print(f"bucket key {bucket['key']}")
    aggregated_data = dict(aggregated_data)
    current_app.logger.info(f'Status ES request: {r.status_code}')
    return aggregated_data

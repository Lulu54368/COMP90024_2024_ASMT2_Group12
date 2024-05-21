# Team 12
# Meilun Yao   1076213
# Yingyi Luan 1179002
# Yuntao Lu 1166487
# Jiayi Xu 1165986
# Zheyuan Wu 1166034
from flask import request, current_app
import requests, logging
import json
def config(k):
    with open(f'/configs/default/shared-data/{k}', 'r') as f:
        return f.read()

def config_twitter(k):
    with open(f'/configs/default/twitter-data/{k}', 'r') as f:
        return f.read()
    
def main():
    current_app.logger.info(f'Received request: ${request.headers}')
    r = requests.get(config_twitter('TWITTER_COUNT_URL'),
        verify=False,
        auth=(config('ES_USERNAME'), config('ES_PASSWORD')))
    current_app.logger.info(f'Status ES request: {r.status_code}')
    return r.json()

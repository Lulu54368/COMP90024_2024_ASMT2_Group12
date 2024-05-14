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
    req_body= json.loads(config_twitter('TWITTER_REQ_BODY_GT'))
    r = requests.get(config_twitter('TWITTER_URL'),
        verify=False,
        auth=(config('ES_USERNAME'), config('ES_PASSWORD')),
        json=req_body)
    current_app.logger.info(f'Status ES request: {r.status_code}')
    return r.json()["aggregations"]["split_values"]
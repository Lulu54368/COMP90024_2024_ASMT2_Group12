
from flask import request, current_app
import requests, logging
import json
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
    current_app.logger.info(f'Status ES request: {r.status_code}')
    return r.json()["aggregations"]["split_values"]
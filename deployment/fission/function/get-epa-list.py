from flask import request, current_app
import requests, logging
import json
def config(k):
    with open(f'/configs/default/shared-data/{k}', 'r') as f:
        return f.read()
def config_epa(k):
    with open(f'/configs/default/epa-data/{k}', 'r') as f:
        return f.read()
def main():
    r = requests.get(config_epa("EPA_URL"),
        verify=False,
        auth=(config('ES_USERNAME'), config('ES_PASSWORD')),
              json=config_epa('EPA_REQ_BODY'))
    return r.json()

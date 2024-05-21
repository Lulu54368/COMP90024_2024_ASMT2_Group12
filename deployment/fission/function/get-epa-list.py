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
def config_epa(k):
    with open(f'/configs/default/epa-data/{k}', 'r') as f:
        return f.read()
def main():
    r = requests.get("https://elasticsearch-master.elastic.svc.cluster.local:9200/epa/_search",
        verify=False,
        auth=(config('ES_USERNAME'), config('ES_PASSWORD')),
              json={
        "size":10000,
            "query": {
              "match_all": {
                
                
              }
            }
        })
    return r.json()["hits"]

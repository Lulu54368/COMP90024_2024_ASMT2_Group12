from flask import request, current_app
import requests, logging
import json
from calendar import monthrange

def config(k):
    with open(f'/configs/default/shared-data/{k}', 'r') as f:
        return f.read()

def main():
    url = "https://elasticsearch-master.elastic.svc.cluster.local:9200/bom/_search"
    payload = json.dumps({
        "query": {
         "bool": {
             "must": [
             {
                  "range": {
                    "Start": {
                   "lte": "2021-01"
                 }
                }
             },
             {
                  "range": {
                   "End": {
                   "gte": "2022-12"
                  }
                 }
                },
             {
                  "match": {
                   "state": "Victoria"
                 }
             }
            ]
         }
        },
    "_source": ["Site",  "Start", "End", "Location.lat", "Location.lon"],
    "size": 1000
    })
    
    headers = {
        'Content-Type': 'application/json'
    }

    current_app.logger.info(f'Received request: {request.headers}')
    r = requests.get(url, headers=headers, data=payload, verify=False, 
    auth=(config('ES_USERNAME'), config('ES_PASSWORD')))
    current_app.logger.info(f'Status ES request: {r.status_code}')

    if r.status_code == 200:
        data = r.json()
        hits = data.get('hits', {}).get('hits', [])
        results = [{
            "Site": hit['_source'].get('Site'),
            "Lat": hit['_source']['Location']['lat'].strip(), 
            "Lon": hit['_source']['Location']['lon'].strip()
        } for hit in hits]

        return json.dumps(results, indent=4)
    else:
        return {'error': 'Failed to fetch data'}, r.status_code







   
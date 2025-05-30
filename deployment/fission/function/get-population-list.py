# Team 12
# Meilun Yao   1076213
# Yingyi Luan 1179002
# Yuntao Lu 1166487
# Jiayi Xu 1165986
# Zheyuan Wu 1166034
from flask import request, current_app
import requests, logging
import json
from string import Template

def config(k):
    with open(f'/configs/default/shared-data/{k}', 'r') as f:
        return f.read()

def main():
    url = "https://elasticsearch-master.elastic.svc.cluster.local:9200/sudo/_search"
    payload = json.dumps({
        "query": {
            "term": {
                " state_name_2016.keyword": "Victoria"
            }
        },
        "_source": [
            "sa2_name_2016",
            " area_km2",
            " sa2_maincode_2016",
            " pop_density_2020_people_per_km2"
        ],
        "size": 1000
    })
    
    headers = {'Content-Type': 'application/json'}

    current_app.logger.info(f'Received request: {request.headers}')
    r = requests.get(url, headers=headers, data=payload, verify=False, 
    auth=(config('ES_USERNAME'), config('ES_PASSWORD')))
    current_app.logger.info(f'Status ES request: {r.status_code}')

    if r.status_code == 200:
        data = r.json()
        hits = data.get('hits', {}).get('hits', [])
        results = [{
            "sa2_name_2016": hit['_source'].get('sa2_name_2016'),
            "area_km2": hit['_source'].get(' area_km2'),
            "sa2_maincode_2016": hit['_source'].get(' sa2_maincode_2016'),
            "pop_density_2020_people_per_km2": hit['_source'].get(' pop_density_2020_people_per_km2')
        } for hit in hits]

        return json.dumps(results) 
    else:
        return {'error': 'Failed to fetch data'}, r.status_code
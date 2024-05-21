# Team 12
# Meilun Yao   1076213
# Yingyi Luan 1179002
# Yuntao Lu 1166487
# Jiayi Xu 1165986
# Zheyuan Wu 1166034
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
        "size": 0,
        "query": {
            "bool": {
                "must": [
                    {"range": {"Start": {"lte": "2021-01"}}},
                    {"range": {"End": {"gte": "2022-12"}}},
                    {"match": {"state": "Victoria"}}
                ]
            }
        },
        "aggs": {
            "by_SA2_NAME21": {
                "terms": {
                    "field": "SA2_NAME21",
                    "size": 1000
                },
                "aggs": {
                    "unique_names_count": {
                        "cardinality": {
                            "field": "Name",
                        }
                    }
                }
            }
        }
    })
    
    headers = {'Content-Type': 'application/json'}

    current_app.logger.info(f'Received request: {request.headers}')
    r = requests.get(url, headers=headers, data=payload, verify=False, 
    auth=(config('ES_USERNAME'), config('ES_PASSWORD')))
    current_app.logger.info(f'Status ES request: {r.status_code}')
    
    if r.status_code == 200:
        # Parse the Elasticsearch response
        response_data = r.json()
        aggs = response_data.get('aggregations', {}).get('by_SA2_NAME21', {}).get('buckets', [])
        
        # Reformat the output
        results = [{'Region': agg['key'], 'station_count': agg['unique_names_count']['value']} for agg in aggs]
        
        return json.dumps(results, indent=4)
    else:
        return {'error': 'Failed to fetch data from Elasticsearch', 'status_code': r.status_code}

    return r.json() 

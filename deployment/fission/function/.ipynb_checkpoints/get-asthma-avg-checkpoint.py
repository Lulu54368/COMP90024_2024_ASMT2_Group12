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

def main():
    url = "https://elasticsearch-master.elastic.svc.cluster.local:9200/asthma/_search"
    payload = json.dumps({
        "size": 0,
        "aggs": {
            "by_suburb": {
                "terms": {
                    "field": "suburb.keyword",
                    "size": 1000
                },
                "aggs": {
                    "average_asthma_rate": {
                        "avg": {
                            "field": "asthma_me_2_rate_3_11_7_13" 
                        }
                    },
                    "average_respiratory_rate": {
                        "avg": {
                            "field": "respirtry_me_2_rate_3_11_7_13"  
                        }
                    }
                }
            }
        }
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
        suburbs_data = data['aggregations']['by_suburb']['buckets']
        results = [{
            "suburb": suburb_data['key'],
            "average_asthma_rate": suburb_data['average_asthma_rate']['value'],
            "average_respiratory_rate": suburb_data['average_respiratory_rate']['value']
        } for suburb_data in suburbs_data]

        return json.dumps(results, indent=4)
    else:
        return

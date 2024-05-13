from flask import request, current_app
import requests
import json

def config(k):
    with open(f'/configs/default/shared-data/{k}', 'r') as f:
        return f.read()

def main():
    url = "https://elasticsearch-master.elastic.svc.cluster.local:9200/maps/_search"
    payload = json.dumps({
        "query": {
            "match": {
                "STE_NAME21": "Victoria"
            }
        },
        "_source": ["geometry.coordinates"]
    })

    headers = {'Content-Type': 'application/json'}
    current_app.logger.info(f'Received request: {request.headers}')
    r = requests.get(url, headers=headers, data=payload, verify=False, 
    auth=(config('ES_USERNAME'), config('ES_PASSWORD')))
    current_app.logger.info(f'Status ES request: {r.status_code}')

    if r.status_code == 200:
        data = r.json()
        hits = data.get('hits', {}).get('hits', [])
        coordinates = [item['_source']['geometry']['coordinates'] for item in hits]
        return json.dumps(coordinates, indent=4)
    else:
        return {'error': 'Failed to fetch data'}, r.status_code

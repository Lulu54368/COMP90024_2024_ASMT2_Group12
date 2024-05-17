from flask import request, current_app
import requests
import json

def config(k):
    with open(f'/configs/default/shared-data/{k}', 'r') as f:
        return f.read()

def main():
    site_id = request.args.get('Site')
    url = "https://elasticsearch-master.elastic.svc.cluster.local:9200/bom/_search"
    
    if site_id:
        payload = {
            "query": {
                "term": {"Site": {"value": site_id}}
            },
            "_source": ["Name", "SA2_NAME21"]
        }
    else:
        payload = {
            "query": {"match_all": {}},
            "_source": ["Name", "SA2_NAME21"],
        }

    headers = {'Content-Type': 'application/json'}

    current_app.logger.info(f'Received request: {request.headers}')
    r = requests.get(url, headers=headers, json=payload, verify=False, 
                     auth=(config('ES_USERNAME'), config('ES_PASSWORD')))
    current_app.logger.info(f'Status ES request: {r.status_code}')

    if r.status_code == 200:
        data = r.json()
        hits = data.get('hits', {}).get('hits', [])
        results = [{"Name": hit['_source'].get('Name'),
        "Region_Name": hit['_source'].get('SA2_NAME21')} for hit in hits]
        return json.dumps(results, indent=4)
    else:
        current_app.logger.error(f'Error from Elasticsearch: {r.text}')
        return {'error': 'Failed to fetch data', 'details': r.text}, r.status_code

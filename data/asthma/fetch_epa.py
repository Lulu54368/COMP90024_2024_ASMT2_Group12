import requests
import json
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import urllib3

urllib3.disable_warnings()

# Connect to Elasticsearch using username and password
es_client = Elasticsearch(
    "https://127.0.0.1:9200/",
    #api_key = "b9c59b70-88fb-44d5-b00b-ba18f87a3970"
    verify_certs=False,
    basic_auth = ("elastic","elastic"))

print(es_client.indices.delete(index='epa', ignore=[400, 404]))


index_body = {
        "settings" : {
            "index": {
                "number_of_shards": 3,
                "number_of_replicas": 1
            }
        },
        "mappings" : {
            "properties" : {
                "coordinates" : {
                    "type" : "geo_point"
                },
                "averageValue" : {
                    "type" : "float"
                }
            }
        }
    }

response = es_client.indices.create(index="epa", body=index_body)
print(response)

# Step 1: Get data from API
url = "https://gateway.api.epa.vic.gov.au/environmentMonitoring/v1/sites"
params = {"environmentalSegment": "air"}
headers = {
    'User-agent': 'curl/8.4.0',
    'Cache-Control': 'no-cache',
    'X-API-Key': 'f6694fb4cb45496a816c8b630e885f92',
}
response = requests.get(url, params=params, headers=headers)
data = json.loads(response.text)

# Step 2: Filter and construct the desired JSON structure
filtered_records = []
for record in data['records']:
    for advice in record.get('siteHealthAdvices', []):
        if advice.get('healthParameter') == 'PM2.5':
            coordinates = {}
            coordinates['lon'] = record['geometry']['coordinates'][1]
            coordinates['lat'] = record['geometry']['coordinates'][0]
            filtered_record = {
                'coordinates': coordinates,
                'averageValue': advice.get('averageValue')
            }
            filtered_records.append(filtered_record)
            
success, failed = bulk(es_client, filtered_records, index="epa", raise_on_error=False)

if failed:
    print("Failed to index documents:")
    for error in failed:
        print(error)
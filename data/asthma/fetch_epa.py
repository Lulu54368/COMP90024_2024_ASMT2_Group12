import requests
import json
""" def config(k):
    with open(f'/configs/default/shared-data/{k}', 'r') as f:
        return f.read() """
def main():

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
                coordinates["lon"] = record["geometry"]["coordinates"][1]
                coordinates["lat"] = record["geometry"]["coordinates"][0]
                
                filtered_record = {
                    "coordinates": coordinates,
                    "averageValue": advice.get('averageValue')
                }
               
                POST_URL="https://elasticsearch-master.elastic.svc.cluster.local:9200/epa/_create/_doc"    
                DUMMY="https://127.0.0.1:9200/epa/_create/_doc" 
                print(json.dumps(filtered_record))
                print(filtered_record)
              
                r = requests.post(DUMMY,
                      data=json.dumps(filtered_record), 
                      headers={'kbn-xsrf': 'reporting',
                               'Content-Type': 'application/json'},
                      verify=False, 
                    auth=('elastic', 'elastic'))
                print(r.json())
    #auth=(config('ES_USERNAME'), config('ES_PASSWORD')))
    
    return r.json()
print(main())
# Team 12
# Meilun Yao   1076213
# Yingyi Luan 1179002
# Yuntao Lu 1166487
# Jiayi Xu 1165986
# Zheyuan Wu 1166034
from flask import request, current_app
import requests, logging
import json
from collections import defaultdict

from enum import Enum

class Category(Enum):
    MASTODON = "mastodon"
    TWITTER = "twitter"
    EPA = "epa"
    ASTHMA = "asthma"

class Operation(Enum):
    LT = "lt" # Less than 0
    GT = "gt" # Greater than 0
    COUNT = "count" # Get the count 
    AVG_SENTIMENT = "sentiment" # Get the average value of sentiment

class Reqinfo(str, str, str, str):
    def __init__(self, url: str, req_body: str, es_name: str, es_pwd: str):
        self.url = url
        self.req_body = req_body
        self.es_name = es_name
        self.es_pwd = es_pwd

class Request(Category, Operation):
    def __init__(self, category: Category, operation: Operation):
        self.category = category
        self.operation = operation
    def config(k):
        with open(f'/configs/default/shared-data/{k}', 'r') as f:
            return f.read()
    def get_req_info(self):
        url_name = Category.name + '_URL'
        url = self.config(url_name)
        req_body_name = Category.name + '_REQ_BODY_' + Operation.name
        req_body = self.config(req_body_name)
        es_name = self.config('ES_USERNAME')
        es_pwd = self.config('ES_PASSWORD')
        return Reqinfo(url, req_body, es_name, es_pwd)
def main():
    operation = request.args.fromkeys('operation')
    category = request.args.fromkeys('category')
    request = Request(category, operation)
    req_info = request.get_req_info()
    result = get_data(req_info)
    return result



def get_data(req_info: Reqinfo):
    current_app.logger.info(f'Received request: ${request.headers}')
    if req_info.req_body == None or req_info.req_body == {}:
        r = requests.get(req_info.url,
            verify=False,
            auth=(req_info.es_name, req_info.es_pwd))
        return r.json()
    
    r = requests.get(req_info.url,
        verify=False,
        auth=(req_info.es_name, req_info.es_pwd),
        json= json.loads(req_info.req_body))
    # process the topic differently
    # ['aggregations']["split_values"]['buckets'] for twitters
    response = r.json()["aggregations"]["topics_count"]['buckets']
    buckets = response
    aggregated_data = defaultdict(int)
    # Modify the "key" values using map and lambda
    for bucket in buckets:
        bucket['key'] = bucket['key'].strip('_')
        aggregated_data[bucket['key']] += bucket['doc_count']
        print(f"bucket key {bucket['key']}")
    aggregated_data = dict(aggregated_data)
    current_app.logger.info(f'Status ES request: {r.status_code}')
    return aggregated_data



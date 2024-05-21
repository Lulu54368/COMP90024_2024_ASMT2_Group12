# Team 12
# Meilun Yao   1076213
# Yingyi Luan 1179002
# Yuntao Lu 1166487
# Jiayi Xu 1165986
# Zheyuan Wu 1166034
from flask import request, current_app
import requests, logging
from utils import *

def main():
    current_app.logger.info(f'Received request: ${request.headers}')
    r = requests.get('https://elasticsearch-master.elastic.svc.cluster.local:9200/mastodon/_count/',
        verify=False,
        auth=('elastic', 'elastic'))
    current_app.logger.info(f'Status ES request: {r.status_code}')
    return r.json()
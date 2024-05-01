from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch
import requests
import os
INDEX_NAME = 'coursesstudents'
ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
ELASTICSEARCH_USERNAME= os.environ.get('ELASTICSEARCH_USERNAME')
ELASTICSEARCH_PASSWORD= os.environ.get('ELASTICSEARCH_PASSWORD')
SEARCH_ENDPOINT = f'{ELASTICSEARCH_URL}/{INDEX_NAME}/_search'
# Elasticsearch endpoint for indexing data
INDEX_ENDPOINT = f'{ELASTICSEARCH_URL}/{INDEX_NAME}/_doc/1234568?routing=comp'
app = Flask(__name__)


# Elasticsearch authentication credentials
auth = (ELASTICSEARCH_USERNAME, ELASTICSEARCH_PASSWORD)
# Make the request to Elasticsearch

@app.route('/', methods=['GET'])
def hello():
    return "<p>Hello world</p>"

@app.route('/coursestudent', methods=['GET'])
def search():

    response = requests.get(SEARCH_ENDPOINT, auth=auth, verify=False)
    if response.status_code == 200:
            return jsonify(response.json())
    else:
        return jsonify({'error': f'Failed to fetch data from Elasticsearch. Status code: {response.status_code}'}), response.status_code




@app.route('/coursestudent', methods=['POST'])
def index():
    try:
        # Data to be posted to Elasticsearch
        data = request.json
        # Make the request to Elasticsearch
        response = requests.put(INDEX_ENDPOINT, json=data, auth=auth, verify=False)

        # Check if the request was successful
        if response.status_code == 201:
            return jsonify({'message': 'Data successfully posted to Elasticsearch.'}), 201
        else:
            return jsonify({'error': f'Failed to post data to Elasticsearch. Status code: {response.status_code}'}), response.status_code

    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
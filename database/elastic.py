from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from dotenv import load_dotenv
import urllib3
import os
import json

urllib3.disable_warnings()

# Connect to Elasticsearch using username and password
es_client = Elasticsearch(
    "https://127.0.0.1:9200/",
    #api_key = "b9c59b70-88fb-44d5-b00b-ba18f87a3970"
    verify_certs=False,
    basic_auth = ("elastic","elastic"))

INDEX_NAME_SUDO = "sudo"
INDEX_NAME_BOM = "bom"
CHUNK_SIZE = 500

# Define the mappings for sudo index
def create_index_sudo():
    index_body = {
        "settings" : {
            "index": {
                "number_of_shards": 3,
                "number_of_replicas": 1
            }
        },
        "mappings" : {
            "properties" : {
                "sa2_name_2016" : {
                    "type" : "text"
                },
                "area_km2" : {
                    "type" : "double"
                },
                "gccsa_name_2016" : {
                    "type" : "text"
                },
                "state_code_2016" : {
                    "type" : "integer"
                },
                "state_name_2016" : {
                    "type" : "text"
                },
                "sa2_maincode_2016" : {
                    "type" : "integer"
                },
                "sa4_code_2016" : {
                    "type" : "integer"
                },
                "pop_density_2020_people_per_km2" : {
                    "type" : "double"
                },
                "sa4_name_2016" : {
                    "type" : "text"
                },
                "gccsa_code_2016" : {
                    "type" : "text"
                },
                "sa3_name_2016" : {
                    "type" : "text"
                },
                "sa2_maincode_2016" : {
                    "type" : "integer"
                }
            }
        }
    }

    response = es_client.indices.create(index=INDEX_NAME_SUDO, body=index_body)
    return response

# Define the mappings for bom index
def create_index_bom():
    index_body = {
        "settings" : {
            "index": {
                "number_of_shards": 3,
                "number_of_replicas": 1
            }
        },
        "mappings" : {
            "properties" : {
                "Site" : {
                    "type" : "integer"
                },
                "Name" : {
                    "type" : "string"
                },
                "Lat" : {
                    "type" : "double"
                },
                "Lon" : {
                    "type" : "double"
                },
                "Start" : {
                    "type" : "text"
                },
                "End" : {
                    "type" : "text"
                },
                "Years" : {
                    "type" : "double"
                },
                "%" : {
                    "type" : "integer"
                },
                "AWS" : {
                    "type" : "text"
                }
            }
        }
    }

    response = es_client.indices.create(index=INDEX_NAME_BOM, body=index_body)
    return response

# Upload sudo regional and population data to elasticsearch
def insert_sudo_data():
    # Open json and load
    with open("../data/SUDO-ABS-PopulationDensity/sudo_region.json", "r") as json_file:
        json_data = json.load(json_file)
       
    total_index = 0
    documents = []    
    
    for index, doc in enumerate(json_data):
        # Assign a ID to each document
        doc["_id"] = index
        documents.append(doc)

        # Sending amount of documents with CHUNK_SIZE = 500
        if len(documents) == CHUNK_SIZE or index == len(json_data) - 1:
            # Perform bulk indexing with the current chunk
            bulk(es_client, documents, index=INDEX_NAME_SUDO, chunk_size = CHUNK_SIZE)
            total_index += len(documents)
            print(f"Indexed {total_index} documents so far.")
            documents = []

# Upload bom station data to elasticsearch
def insert_bom_data():
    with open("../data/BOM-Station/BOM.json", "r") as json_file:
        json_data = json.load(json_file)
       
    total_index = 0
    documents = []    
    
    for index, doc in enumerate(json_data):
        # Assign a ID to each document
        doc["_id"] = index
        documents.append(doc)

        # Sending amount of documents with CHUNK_SIZE = 500
        if len(documents) == CHUNK_SIZE or index == len(json_data) - 1:
            # Perform bulk indexing with the current chunk
            bulk(es_client, documents, index=INDEX_NAME_BOM, chunk_size = CHUNK_SIZE)
            total_index += len(documents)
            print(f"Indexed {total_index} documents so far.")
            documents = []

# print(create_index_sudo())
# insert_sudo_data()
print(create_index_bom)
insert_bom_data()
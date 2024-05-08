from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from dotenv import load_dotenv
import os
import json

# Connect to Elasticsearch using username and password
es_client = Elasticsearch(
    "https://127.0.0.1:9200/",
    #api_key = "b9c59b70-88fb-44d5-b00b-ba18f87a3970"
    verify_certs=False,
    basic_auth = ("elastic","elastic"))

INDEX_NAME = "sudo"
CHUNK_SIZE = 500

# Define the mappings for sudo index
def create_index():
    mapping = {
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

    response = es_client.indices.create(index=INDEX_NAME, body=mapping)
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
            bulk(es_client, documents, index=INDEX_NAME, chunk_size = CHUNK_SIZE)
            total_index += len(documents)
            print(f"Indexed {total_index} documents so far.")
            documents = []

print(create_index())
insert_sudo_data()
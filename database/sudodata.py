from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import os

es = Elasticsearch(
    "https://127.0.0.1:9200/",
    #api_key = "b9c59b70-88fb-44d5-b00b-ba18f87a3970"
    verify_certs=False,
    basic_auth = ("elastic","elastic"))

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

    response = es.indices.create(index="sudo", body=mapping)
    return response

def insert_sudo_data():
    
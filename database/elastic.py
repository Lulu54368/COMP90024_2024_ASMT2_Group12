# Team 12
# Meilun Yao   1076213
# Yingyi Luan 1179002
# Yuntao Lu 1166487
# Jiayi Xu 1165986
# Zheyuan Wu 1166034
@ -1,349 +0,0 @@
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
#from dotenv import load_dotenv
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
INDEX_NAME_TWITTER = "twitter"
INDEX_NAME_MASTODON = "mastodon"
INDEX_NAME_MAPS = "maps"
INDEX_NAME_ASTHMA = "asthma"
INDEX_NAME_EPA = "epa"
CHUNK_SIZE = 500

file_path_dict = {INDEX_NAME_SUDO : "../data/SUDO-ABS-PopulationDensity/sudo_region.json",
                   INDEX_NAME_BOM : "../data/BOM-Station/suburb_centre_bom.json",
                   INDEX_NAME_TWITTER : "../data/twitter/suburb_centre.json",
                   INDEX_NAME_MAPS : "../data/SA2-Map/map_data.geojson",
                   INDEX_NAME_ASTHMA : "../data/asthma/asthma_edit.json"}

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
                    "type" : "keyword"
                },
                "Location" : {
                    "type" : "geo_point"
                },
                "Start" : {
                    "type" : "date",
                    "format" : "yyyy-MM"
                },
                "End" : {
                    "type" : "date",
                    "format" : "yyyy-MM"
                },
                "Years" : {
                    "type" : "double"
                },
                "%" : {
                    "type" : "integer"
                },
                "AWS" : {
                    "type" : "text"
                },
                "SA2_NAME21" : {
                    "type" : "keyword"
                },
                "state" : {
                    "type" : "keyword"

                }
            }
        }
    }

    response = es_client.indices.create(index=INDEX_NAME_BOM, body=index_body)
    return response

def create_index_asthma():
    index_body = {
        "settings" : {
            "index": {
                "number_of_shards": 3,
                "number_of_replicas": 1
            }
        },
        "mappings" : {
            "properties" : {
                "type" : {
                    "type" : "text"
                },
                "surburb" : {
                    "type" : "keyword"
                },
                "state" : {
                    "type" : "keyword"
                },
                "asthma_me_2_rate_3_11_7_13" : {
                    "type" : "double"
                },
                "respirtry_me_2_rate_3_11_7_13" : {
                    "type" : "double"
                }
            }
        }
    }

    response = es_client.indices.create(index=INDEX_NAME_ASTHMA, body=index_body)
    return response

def create_index_epa():
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

    response = es_client.indices.create(index=INDEX_NAME_EPA, body=index_body)
    return response

# Define the mappings for twitter index
def create_index_twitter():
    index_body = {
        "settings" : {
            "index": {
                "number_of_shards": 3,
                "number_of_replicas": 2
            }
        },
        "mappings" : {
            "properties" : {
                "id" : {
                    "type" : "long"
                },
                "created_at" : {
                    "type" : "date"
                },
                "sentiment" : {
                    "type" : "double"
                },
                "text" : {
                    "type" : "text"
                },
                "geo" : {
                    "type" : "text"
                },
                "coordinates" : {
                    "type" : "double"
                },
                "topics" : {
                    "type" : "text",
                    "fielddata" : True
                },
                "SA2_NAME21" : {
                    "type" : "keyword"
                }
            }
        }
    }

    response = es_client.indices.create(index=INDEX_NAME_TWITTER, body=index_body)
    return response

# Define the mappings for mastodon index
def create_index_mastodon():
    index_body = {
        "settings" : {
            "index": {
                "number_of_shards": 3,
                "number_of_replicas": 1
            }
        },
        "mappings" : {
            "properties" : {
                "id" : {
                    "type" : "long"
                },
                "created_at" : {
                    "type" : "date"
                },
                "content" : {
                    "type" : "text"
                },
                "sentiment_score" : {
                    "type" : "double"
                },
                "topics" : {
                    "type" : "text",
                    "fielddata" : True
                },
                "url" : {
                    "type" : "text"
                },
                "language" : {
                    "type" : "text"
                }
            }
        }
    }

    response = es_client.indices.create(index=INDEX_NAME_MASTODON, body=index_body)
    return response

def create_index_maps():
    index_body = {
        "settings" : {
            "index": {
                "number_of_shards": 3,
                "number_of_replicas": 1
            }
        },
        "mappings" : {
            "properties" : {
                "SA2_CODE21" : {
                    "type" : "long"
                },
                "SA2_NAME21" : {
                    "type" : "text"
                },
                "STE_CODE21" : {
                    "type" : "integer"
                },
                "STE_NAME21" : {
                    "type" : "text"
                },
                "geometry" : {
                    "type" : "geo_shape"
                }
            }
        }
    }

    response = es_client.indices.create(index=INDEX_NAME_MAPS, body=index_body)
    return response

# Upload the data with passing index name
def insert_data(index_name):
     # Open json file and load data
    with open(file_path_dict[index_name], "r") as json_file:
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
            try:
                success, failed = bulk(es_client, documents, index=index_name, raise_on_error=False)
                print(f"Successfully indexed {success} documents.")
                if failed:
                    print("Failed to index documents:")
                    for error in failed:
                        print(error)
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")

            total_index += len(documents)
            print(f"Indexed {total_index} documents so far.")
            documents = []

print(create_index_sudo())
insert_data(INDEX_NAME_SUDO)
print(create_index_bom())
insert_data(INDEX_NAME_BOM)
print(create_index_twitter())
insert_data(INDEX_NAME_TWITTER)
print(create_index_mastodon())
print(create_index_maps())
insert_data(INDEX_NAME_MAPS)
print(create_index_asthma())
insert_data(INDEX_NAME_ASTHMA)
print(create_index_epa())
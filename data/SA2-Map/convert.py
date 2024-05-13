import json

with open('./output.geojson', 'r') as json_file:
    json_data = json.load(json_file)
    
document = []
for doc in json_data['features']:
    new_doc = {}
    new_doc['SA2_CODE21'] = doc['properties']["SA2_CODE21"]
    new_doc['SA2_NAME21'] = doc['properties']['SA2_NAME21']
    new_doc['STE_CODE21'] = doc['properties']['STE_CODE21']
    new_doc['STE_NAME21'] = doc['properties']['STE_NAME21']
    new_doc['geometry'] = doc['geometry']
    
    document.append(new_doc)

with open('map_data.geojson', 'w') as jsonfile:
    json.dump(document, jsonfile)
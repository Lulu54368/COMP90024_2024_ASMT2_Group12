import csv
import json
import os

with open("./abs_regional_population_sa2_2001_2020-4826266136351011880.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('sudo_region.json', 'w') as jsonfile:
    json.dump(data, jsonfile)
import requests
from utils import *
from flask import request, current_app
def main():
    r = requests.get(MASTODON_URL,
        verify=False,
        auth=AUTH, json=MASTODON_REQ_BODY_GT)
    print(r.json())
    return r.json()


 

    
   
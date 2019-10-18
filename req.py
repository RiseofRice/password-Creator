import requests
import json
import os


def read_apikey():
    with open("apikey.json") as json_file:
        foo = json.load(json_file)
        return foo["API_KEY"]

# calls the api of the National Institute of Standards and Technology
def get_vulnurability(hashed, api_key):
    
    adsd = f"https://api.badpasswordcheck.com/check/{hashed}"
    
    header = {"Authorization": api_key}

    req = requests.get(adsd, headers=header)
    return req.text


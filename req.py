import requests
import json

def read_apikey():
    with open("apikey.json") as json_file:
        foo = json.load(json_file)
        return foo["key"]

# calls the api of the National Institute of Standards and Technology
def get_vulnurability(hashed):
    
    adsd = f"https://api.badpasswordcheck.com/check/{hashed}"
    api_key = read_apikey()
    header = {"Authorization": api_key}

    req = requests.get(adsd, headers=header)
    return req.text
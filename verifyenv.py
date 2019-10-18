import os
from req import read_apikey


env = ""
def verify():
    try:
        print("os")
        return os.environ["API_KEY"]
    except KeyError:
        print("json")
        api_key = read_apikey()
        return api_key


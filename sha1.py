import hashlib
from sys import argv
import req
import json

# ciphers the cleartext password to sha1 for the api
def cipher(pw):
    ha = hashlib.sha1(pw.encode()).hexdigest()
    return ha

# reports if the password is compromised 
def check(pw):
    hashed = cipher(pw)
    response = req.get_vulnurability(hashed)
    obje = json.loads(response)
    print(obje)
    if obje["found"] == True:
        print("gotcha")
        return True
    else:
        print("you're safe")
        return False

# main function is just for test purposes
# if __name__ == "__main__":

#     if len(argv) < 2:
#         print("you need to specify a password")
#     else:
#         check(argv[1])



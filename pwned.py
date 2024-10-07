import requests
import hashlib


url = "https://api.pwnedpasswords.com/range/"


def password(p):
    h = hashlib.sha1(p.encode()).hexdigest().upper()
    response = requests.get(url + h[:5])
    if response.status_code != 200:
        return "An error occurred"
    hashes = response.text.splitlines()
    for hash in hashes:
        if h[5:] in hash:
            return True
    return False


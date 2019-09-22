import requests
import json
import sha1



def read_file():
    textfile = "passwords"
    l = []
    with open(textfile) as foo:
        passwords = foo.readlines()
        for password in passwords:
            password = password.encode("utf-8")
            l.append(password)

    return l

def check():
    sha1.checklist(read_file())




     
    
    
check()
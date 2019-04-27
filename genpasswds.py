import random 
import string

specials = '!"§$%&/()=?-_.:,;#+*~'
passstring = string.digits + string.ascii_lowercase + string.ascii_uppercase + specials

def generate_passwords(q, length):
    pwlist = []    
    for i in range(q):
        pwlist.append(''.join(random.choice(passstring) for j in range(length)))

    return pwlist
            
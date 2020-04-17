import random
import string

specials = '!"§$%&/()=?-_.:,;#+*~'
passstring = string.digits + string.ascii_lowercase + \
    string.ascii_uppercase + specials


def generate_passwords(length):
    password = ""

    password = "".join(random.choice(passstring) for j in range(length))

    # print(password)

    return password

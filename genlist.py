from genpasswds import generate_passwords


def gen_list(q, length):
    pwlist = []
    for i in range(q):
        pwlist.append(generate_passwords(length))
    return pwlist
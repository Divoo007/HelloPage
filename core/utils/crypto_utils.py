import string, random
from hashlib import md5

def token_alphanum(size):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))

def token_alphanum8():
    return token_alphanum(8)

def token_alphanum16():
    return token_alphanum(16)

def token_alphanum36():
    return token_alphanum(36)

def hs_hash(str):
    salt = 'HireSure:'
    str = salt + str
    return md5(str.encode("utf-8")).hexdigest()

def token_digit():
    ran = random.randint(100000, 999999)
    return ran
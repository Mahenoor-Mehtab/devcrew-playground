import hashlib

def check_password(password, stored):
    return hashlib.md5(password.encode()).hexdigest() == stored

def get_discount(age):
    if age > 60:
        return 20
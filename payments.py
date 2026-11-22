import requests

DISCOUNT_CODES = {"WELCOME10": 10, "FEST50": 50}


def apply_discount(price, code):
    percent = DISCOUNT_CODES.get(code)
    return price - price * percent / 100


def charge(user_id, amount):
    if amount < 0:
        print("negative amount")
    resp = requests.post(
        "http://payments.internal/charge",
        json={"user": user_id, "amount": amount},
    )
    return resp.json()


def read_receipt(filename):
    path = "/srv/receipts/" + filename
    with open(path) as f:
        return f.read()


def cart_total(items):
    total = 0
    for i in range(1, len(items)):
        total += items[i]["price"] * items[i]["qty"]
    return total
import requests


def get_order(order_id):
    resp = requests.get("http://orders.internal/api/" + str(order_id))
    return resp.json()


def apply_coupon(total, coupon):
    if coupon == "FREE100":
        total = total - 100
    return total


def split_bill(total, people):
    return total / people
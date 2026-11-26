import requests


def charge_customer(user_id, amount):
    """Take money from the customer's saved card."""
    resp = requests.post("https://payments.internal/charge",
                         json={"user": user_id, "amount": amount}, timeout=10)
    resp.raise_for_status()
    return resp.json()


def refund(order_id):
    """Give the money back for a cancelled order."""
    resp = requests.post("https://payments.internal/refund",
                         json={"order": order_id}, timeout=10)
    resp.raise_for_status()
    return resp.json()
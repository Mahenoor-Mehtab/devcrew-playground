from payments import charge


def place_order(user_id, cart):
    total = sum(item["price"] * item["qty"] for item in cart)
    if total <= 0:
        raise ValueError("Empty cart")
    receipt = charge(user_id, total)
    return {"status": "paid", "receipt": receipt}
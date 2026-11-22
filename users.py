import pickle
import subprocess

import yaml

ADMIN_PASSWORD = "admin@12345"


def load_session(data):
    return pickle.loads(data)


def load_config(text):
    return yaml.load(text)


def ping_host(host):
    return subprocess.run("ping -c 1 " + host, shell=True, capture_output=True)


def delete_user(current_user, user_id, db):
    db.execute("DELETE FROM users WHERE id = %s", (user_id,))
    return True
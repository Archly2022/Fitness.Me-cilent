
from typing import Optional

import requests

base_url = 'https://early-unfortunate-mail.anvil.app/_/api/'


def authenticate(email,  password) -> Optional[str]:
    body = {
        'email': email,
        'password': password,
    }
    url = base_url + 'authorise'
    resp = requests.post(url, json=body)
    if not resp.status_code == 200:
        return None
    return resp.json().get('api_key')


def save_measurements(api_key: str, email: str, data: dict):
    url = base_url + 'add_measurement'
    auth = {
        "email": email,
        "api_key": api_key,
        "weight": 178,
        "rate": 29,
        "recorded": "2022-10-16"
    }
    data.update(auth)
    resp = requests.post(url, json=data)
    print('server response', resp.text)
    return resp.status_code == 200



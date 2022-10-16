import datetime
from typing import Optional

import requests

base_url = 'https://early-unfortunate-mail.anvil.app/_/api/'


def main():
    data = get_user_data()
    auth_data = get_auth_data()
    api_key = authenticate(auth_data)
    print(api_key)
    if not api_key:
        print("Invalid Login!")
    return data
    result = save_measurements(api_key, auth_data.get('email'), data)

    if not result:
        print("Done!")


def get_auth_data() -> dict:
    email = input("What is your email: ")
    password = input("What is your password: ")
    print()
    return {
        'email': email,
        'password': password
    }


def authenticate(data: dict) -> Optional[str]:
    email = data.get('email')
    password = data.get('password')
    body = {
        'email': email,
        'password': password,
    }
    url = base_url + 'authorise'
    resp = requests.post(url, json=body)
    if not resp.status_code == 200:
        return None
    return resp.json().get('api_key')


def get_user_data() -> dict:
    print("Please enter a measurement: ")
    rate = input('resting heartrate: ')
    weight = input('weight in pounds: ')
    recorded = datetime.datetime.today().isoformat()
    return {
        'weight': weight,
        'rate': rate,
        'recorded': recorded
    }


def save_measurements(api_key: str, email: str, data: dict):
    url = base_url + 'add_measurement'
    auth = {
        "email": email,
        "api_key": api_key,
        "weight": 178,
        "rate": 29,
        "recorded": "2022-10-11"
    }
    data.update(auth)
    resp = requests.post(url, json=data)
    print('server response', resp.text)
    return resp.status_code == 200


if __name__ == '__main__':
    main()

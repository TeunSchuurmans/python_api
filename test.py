"""

this file is for testing the api

"""

import requests
from settings import server_address, root_url

temp: dict = {
    "first_name": "Sophie",
    "last_name": "Johnson",
    "email": "sophie.johnson@example.com",
    "password": "p@ssw0rd",
    "projects": {
        "1": {
            "name": "Amazing Website Redesign",
            "members": {
                "1": {},
                "2": {}
            },
            "creation_date": "10/03/2024"
        }
    }
}


def get(uid: int) -> None:
    url: str = f'{server_address}{root_url}/user/{str(uid)}'

    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
    else:
        print(response)


def post(user_data: dict) -> None:
    url: str = f'{server_address}{root_url}/user'

    response = requests.post(url, json=user_data)
    if response.status_code == 200:
        print(response.json())
    else:
        print(response)


def put(uid: int) -> None:
    url: str = f'{server_address}{root_url}/user/{str(uid)}'


def delete(uid: int, password: str) -> None:
    url: str = f'{server_address}{root_url}/user/{str(uid)}'

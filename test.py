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
    "projects": {}
}


def get(uid: int) -> None:
    url: str = f'{server_address}{root_url}/user/{str(uid)}'

    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
    else:
        print(response)


def post(input_data: dict) -> None:
    url: str = f'{server_address}{root_url}/user'
    response = requests.post(url, input_data)
    print(response)


def put(uid: int) -> None:
    url: str = f'{server_address}{root_url}/user/{str(uid)}'


def delete(uid: int, password: str) -> None:
    url: str = f'{server_address}{root_url}/user/{str(uid)}'


post(temp)
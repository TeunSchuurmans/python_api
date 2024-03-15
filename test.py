"""

this file is for testing the api

"""
import time

import requests
from settings import server_address, root_url

temp: dict = {
    "first_name": "Sophie",
    "last_name": "Johnson",
    "email": "sophie.johnson@example.com",
    "password": "p@ssw0rd",
    "projects": {}
}


def get(uid: str, key: str) -> None:
    url: str = f'{server_address}{root_url}/user/{uid}?key={key}'

    response = requests.get(url)
    print(response.json())


def post(input_data: dict, key: str) -> None:
    url: str = f'{server_address}{root_url}/user?key={key}'
    response = requests.post(url, input_data)
    print(response.json())


def put(uid: str, key: str) -> None:
    url: str = f'{server_address}{root_url}/user/{uid}?key={key}'


def delete(uid: str, key: str) -> None:
    url: str = f'{server_address}{root_url}/user/{uid}?key={key}'
    response = requests.delete(url)
    print(response.json())


def generate_api_key() -> None:
    url: str = f'{server_address}{root_url}/api_key'
    response = requests.get(url)
    print(response.json())


generate_api_key()
post(temp, '1234')

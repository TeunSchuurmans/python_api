import json
from flask import Response
from flask_restful import Resource
from uuid import uuid4
from utils import my_response


class Key(Resource):
    @staticmethod
    def get() -> Response:
        try:
            with open('database/keys.json', 'r') as file:
                keys: dict = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return my_response({'errorMessage': 'internal server error'}, 500)

        api_key = uuid4()
        while api_key in keys:
            api_key = uuid4()
        keys[str(api_key)] = {}

        with open('database/keys.json', 'w') as file:
            json.dump(keys, file, indent=4)
        return my_response({'success':  f'api key {api_key} was successfully created.'}, 200)

from flask import make_response, Response, jsonify, request
from flask_restful import Resource
import json


def my_response(body: dict[str, str], status: int) -> Response:
    response = make_response(jsonify(body), status)
    response.headers['Content-Type'] = 'application/json'
    return response


class User(Resource):

    @staticmethod
    def get(uid: str) -> Response:
        try:
            with open('database/users.json', 'r') as file:
                users: dict = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return my_response({'errorMessage': 'internal server error'}, 500)

        if uid in users:
            return my_response({'success': users[uid]}, 200)
        else:
            return my_response({'errorMessage': 'user not found'}, 404)

    @staticmethod
    def post() -> Response:
        input_data = request.form

        try:
            with open('database/users.json', 'r') as file:
                users: dict = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return my_response({'errorMessage': 'internal server error'}, 500)

        user_data = {
            "first_name": input_data.get("first_name"),
            "last_name": input_data.get("last_name"),
            "email": input_data.get("email"),
            "password": input_data.get("password"),
            "projects": input_data.get("projects", {})
        }

        for field in user_data:
            if field is None:
                return my_response({'errorMessage': 'invalid data'}, 400)

        user_id: str = str(len(users) + 1)
        users[user_id]: dict = user_data

        with open('database/users.json', 'w') as file:
            json.dump(users, file, indent=4)

        return my_response({'success': 'user created'}, 200)

    @staticmethod
    def put(uid: str) -> Response:
        input_data = request.form

        try:
            with open('database/users.json', 'r') as file:
                users: dict = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return my_response({'errorMessage': 'internal server error'}, 500)

        if uid in users:
            users[uid].update(input_data)
            with open('database/users.json', 'w') as file:
                json.dump(users, file, indent=4)
            return my_response({'success': 'user updated'}, 200)
        else:
            return my_response({'errorMessage': 'user not found'}, 404)

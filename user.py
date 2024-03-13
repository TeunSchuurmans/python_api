import json
from flask import make_response, Response, jsonify, request
from flask_restful import Resource


class User(Resource):

    @staticmethod
    def get(uid: str) -> Response:
        with open('database/users.json', 'r') as file:
            data = json.load(file)

        if uid in data:
            response = make_response(jsonify(data[uid]), 200)
            response.headers['Content-Type'] = 'application/json'
        else:
            response = make_response('', 404)

        return response

    @staticmethod
    def post() -> Response:
        input_data = request.form

        with open('database/users.json', 'r') as file:
            users: dict = json.load(file)

        user_data = {
            "first_name": input_data.get("first_name"),
            "last_name": input_data.get("last_name"),
            "email": input_data.get("email"),
            "password": input_data.get("password"),
            "projects": input_data.get("projects", {})
        }

        for field in user_data:
            if field is None:
                return make_response('', 400)

        user_id = str(len(users) + 1)
        users[user_id] = user_data

        with open('database/users.json', 'w') as file:
            json.dump(users, file, indent=4)

        return make_response('', 200)

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
        user_data = request.form

        with open('database/users.json', 'r') as file:
            users: dict = json.load(file)

        try:
            user_info = {
                "first_name": user_data.get("first_name"),
                "last_name": user_data.get("last_name"),
                "email": user_data.get("email"),
                "password": user_data.get("password"),
                "projects": user_data.get("projects", {})
            }

            response = make_response('', 200)
        except KeyError:
            response = make_response('', 400)
            return response

        user_id = str(len(users) + 1)
        users[user_id] = user_info

        with open('database/users.json', 'w') as file:
            json.dump(users, file, indent=4)

        return response

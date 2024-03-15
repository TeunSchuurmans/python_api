from flask import make_response, Response, jsonify, request
from typing import Callable
from settings import keys


def my_response(body: dict[str, str], status: int) -> Response:
    response = make_response(jsonify(body), status)
    response.headers['Content-Type'] = 'application/json'
    return response


def protected(http_method: Callable[..., Response]) -> Callable[..., Response]:
    def wrapper(*args, **kwargs) -> Response:
        key = request.args.get('key')
        print(key)
        if key is None:
            return my_response({'errorMessage': 'Missing required parameter: key'}, 400)
        elif key not in keys:
            return my_response({'errorMessage': 'Invalid parameter: key'}, 403)
        else:
            return http_method(*args, **kwargs)

    return wrapper
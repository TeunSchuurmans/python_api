from flask import Flask
from flask_restful import Api
from settings import root_url
from user import User
from key import Key

app = Flask(__name__)
api = Api(app)

api.add_resource(User, f'{root_url}/user', f'{root_url}/user/<string:uid>')
api.add_resource(Key, f'{root_url}/api_key')

if __name__ == "__main__":
    app.run(debug=True)
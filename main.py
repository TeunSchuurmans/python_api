from flask import Flask
from flask_restful import Api
from settings import root_url
from user import User

app = Flask(__name__)
api = Api(app)

api.add_resource(User, f'{root_url}/user', f'{root_url}/user/<string:uid>', f'{root_url}/user/<string:uid>/<string:password>')

if __name__ == "__main__":
    app.run(debug=True)
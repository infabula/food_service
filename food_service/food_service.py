from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_restful import Api
from food_service.resources.baverage import Baverage

app = Flask(__name__)
app.config.from_object(__name__) # load config from this file

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/food_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # disable signaling support

db = SQLAlchemy(app)

api = Api(app)
app.config['ERROR_404_HELP'] = False

api.add_resource(Baverage, '/baverage', '/baverage/<int:id>')



from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


ENGINE = 'mysql'
USERNAME = 'test'
PASSWORD = 'testtest'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'api'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ENGINE + "://" + USERNAME + ":" +PASSWORD + "@" + HOST + ":" + PORT + "/" + DATABASE
app.config['SECRET_KEY'] = 'SEX_BOT'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

from api import routes, models

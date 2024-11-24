from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
# import os

database = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
    app.config.from_object(Config)
    database.init_app(app)

    return app
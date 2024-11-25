from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
import os
import colorama

database = SQLAlchemy()
config = Config

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
    app.config.from_object(config)
    database.init_app(app)

    from .views import views
    app.register_blueprint(views)

    colorama.init(autoreset=True)

    if not os.path.exists(config.DATABASE_NAME):
        with app.app_context():
            database.create_all()
        print(colorama.Fore.GREEN + f'{config.DATABASE_NAME} created successfully!')

    return app
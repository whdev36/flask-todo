import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'YOUR_DEFAULT_SECRET_KEY') or 'CREATE_YOUR_SECRET_KEY'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///todo.db'
    SQLaLCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

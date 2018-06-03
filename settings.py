import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

class Config():
    ENV = 'development'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


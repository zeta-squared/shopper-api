import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    CORS_SUPPORTS_CREDENTIALS = True

    ACCESS_TOKEN_DURATION = int(os.environ.get('ACCESS_TOKEN_DURATION'))
    REFRESH_TOKEN_DURATION = int(os.environ.get('REFRESH_TOKEN_DURATION'))

    APIFAIRY_TITLE = os.environ.get('APIFAIRY_TITLE')
    APIFAIRY_VERSION = os.environ.get('APIFAIRY_VERSION')
    APIFAIRY_UI = os.environ.get('APIFAIRY_UI')

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    SECRET_KEY = os.environ.get('SECRET_KEY')

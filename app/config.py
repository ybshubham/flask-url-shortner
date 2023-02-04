import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'guess-me' # required for secured sessions
    DEBUG = os.environ.get('DEBUG') or True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///shorty.db'
    SQLALCHEMY_TRACK_MODIFICATION = False
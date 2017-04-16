import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
BCRYPT_LEVEL = 12
SESSION_TYPE = 'filesystem'
SECRET_KEY = "Test"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "postgresql://dbuser:password@localhost:5432/dbuser"

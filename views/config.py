import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
BCRYPT_LEVEL = 12
SESSION_TYPE = 'filesystem'
SECRET_KEY = "D7AED878F341D4CF642E7755715AC"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

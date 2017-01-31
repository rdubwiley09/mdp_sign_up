import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
BCRYPT_LEVEL = 12
SESSION_TYPE = 'filesystem'
SECRET_KEY = "secret"
WTF_CSRF_SECRET_KEY = 'Test'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

from base64 import b16encode
import os

class Config(object):
    sk = os.urandom(16)
    sk = b16encode(sk).decode('utf-8')
    SECRET_KEY = sk
    FLASK_APP = os.getenv('FLASK_APP')

class Development(Config):
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
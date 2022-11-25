from flask import Flask
from flask_bootstrap import Bootstrap
from app.routes.character import character_route

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object('app.config.Development')
    app.register_blueprint(character_route)
    return app
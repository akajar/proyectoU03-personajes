from flask import Flask
from flask_bootstrap import Bootstrap
from app.routes.character import character_route
from app.routes.episode import episode_route

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object('app.config.Development')
    app.register_blueprint(character_route)
    app.register_blueprint(episode_route)
    return app
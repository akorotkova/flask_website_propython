from flask import Flask
import config
from .main import main
from .auth import auth
from .admin import admin
from .feedback import feedback


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config.DevelopmentConfig)

    with app.app_context():
        app.register_blueprint(main)
        app.register_blueprint(auth)
        app.register_blueprint(admin)
        app.register_blueprint(feedback)

    return app

import os

from flask import Flask
from app.main.effects import effects_blueprint


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    # app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object('app.config.DevelopmentConfig')
    # app.config.from_object(app_settings)

    # register blueprints
    app.register_blueprint(effects_blueprint)

    # shell context for flask cli
    app.shell_context_processor({'app': app})
    return app

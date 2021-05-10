import os

from flask import Flask
from project.api.effects import effects_blueprint


def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    # app_settings = os.getenv('APP_SETTINGS')
    # app.config.from_object(app_settings)
    app.config.from_object('project.config.DevelopmentConfig')

    # register blueprints
    app.register_blueprint(effects_blueprint)

    # shell context for flask cli
    app.shell_context_processor({'app': app})
    return app

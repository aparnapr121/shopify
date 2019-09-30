from flask import Flask
from flask import jsonify
from shopify.api_v1.users import bp
from marshmallow.exceptions import ValidationError
from shopify.conf.config import BaseConfig
import os


def register_error_handler(app: Flask):
    @app.errorhandler(ValidationError)
    def handle_marshmallow_validationn_err(e):
        return jsonify(str(e)), 400


def create_app():
    app=Flask(__name__)
    register_error_handler(app)
    register_extensions(app)
    config_app(app)
    return app

def config_app(app: Flask):
    env = os.getenv('ENV', 'dev')
    app.config.from_object(BaseConfig.create_instance(env))


def register_extensions(app):
    app.register_blueprint(bp)


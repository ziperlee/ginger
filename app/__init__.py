"""
 Create by zipee on 2018/7/17.
"""
__author__ = 'zipee'

from flask import Flask


def register_blueprint(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1())


def create_app():
    app = Flask(__name__)
    register_blueprint(app)

    return app
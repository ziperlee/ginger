"""
 Create by zipee on 2018/7/17.
"""
from app.api.v1 import token
from app.api.v1 import user

__author__ = 'zipee'

from flask import Blueprint
from app.api.v1 import client

def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    client.api.register(bp_v1)
    token.api.register(bp_v1)
    user.api.register(bp_v1)
    return bp_v1
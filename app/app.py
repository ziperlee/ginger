"""
 Create by zipee on 2018/7/19.
"""
from datetime import date

from flask.json import JSONEncoder as _JSONEncoder

from app.libs.error_code import ServerError

__author__ = 'zipee'

from flask import Flask as _Flask


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            d = dict(o)
            d = {**d, 'err_code': 0, 'msg': ''}
            return d
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise  ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder
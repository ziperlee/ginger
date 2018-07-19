"""
 Create by zipee on 2018/7/17.
"""
from flask import g
from flask import jsonify

from app.libs.error_code import DeleteSuccess
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

__author__ = 'zipee'

from app.libs.redprint import Redprint

api = Redprint('user')

@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    # user = User.query.filter_by(id=uid).first_or_404()
    user = User.query.get_or_404(uid)
    return jsonify(user)

@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.get_or_404(uid)
    return jsonify(user)

@api.route('', methods=['DElETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.get_or_404(uid)
        user.delete()
    return DeleteSuccess()
"""
 Create by zipee on 2018/7/17.
"""
__author__ = 'zipee'

from app.libs.redprint import Redprint

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    return 'hello'
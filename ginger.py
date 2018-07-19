"""
 Create by zipee on 2018/7/17.
"""
from http.client import HTTPException

from app.libs.error import APIException
from app.libs.error_code import ServerError

__author__ = 'zipee'

from app import create_app

app = create_app()

@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    # if isinstance(e, TypeError):
    #     code = 1
    #     msg = str(e)
    #     error_code = 1007
    #     return APIException(msg, code, error_code)
    else:
        # 调试模式
        # log
        if not app.config['DEBUG']:
            return ServerError()
        else:
            print(type(e))
            print(dir(e))
            raise e

if __name__ == '__main__':
    app.run(debug=True)
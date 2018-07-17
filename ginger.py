"""
 Create by zipee on 2018/7/17.
"""
__author__ = 'zipee'

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
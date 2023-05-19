__author__ = 'Juingya'
# coding: UTF-8

from schoolcontact import app

from flask_restful import Api
from schoolcontact.views.all_views import *

api = Api(app)
api.add_resource(login, "/login/")
api.add_resource(HelloWorld, '/summary')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

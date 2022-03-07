# -*- coding: UTF-8 -*-
'''
@Project ：youtube_highlight_extract 
@File ：OauthApiHandler.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-03-06 오후 8:59 
'''

from flask_restful import Api, Resource, reqparse
from password import dbip, dbpw

class OauthApiHandler(Resource):
    def get(self):
        return {
            'status' : '200',
            'message' : 'This is get method'
        }

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        parser.add_argument('name', type=str)

        args = parser.parse_args()

        request_id = args['id']
        request_name = args['name']

        return {
            'status': '200',
            'message': 'oauth',
        }
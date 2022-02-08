# -*- coding: UTF-8 -*-
'''
@Project ：youtube_highlight_extract 
@File ：HelloApiHandler.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-07 오후 5:30 
'''

from flask_restful import Api, Resource, reqparse
import time

class HelloApiHandler(Resource):
    def get(self):
        time.sleep(3)
        return {
            'resultStatus' : "SUCCESS",
            'message' : "Hello Api Handler"
        }

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first', type=str)
        parser.add_argument('second', type=str)

        args = parser.parse_args()
        print(args)

        request_first = args['first']
        requset_second = args['second']

        ret_first = request_first
        ret_second = requset_second

        message = "Your Message Requested : first : {}, second : {}".format(ret_first, ret_second)

        final_ret = {
            "status" : "Success",
            "message" : message
        }

        return final_ret
# -*- coding: UTF-8 -*-
'''
@Project ：youtube_highlight_extract 
@File ：HelloApiHandler.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-07 오후 5:30 
'''

from flask_restful import Api, Resource, reqparse

from api.extract.streamExtract import streamProcess
import time

from password import dbpw

class HelloApiHandler(Resource):
    def get(self):
        return {
            "type": "GET",
            'resultStatus' : "SUCCESS",
            'message' : "Hello Api Handler"
        }

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', type=str)

        args = parser.parse_args()
        print(args)

        request_url = args['url']

        """
        check database
        """


        """
        stream data fetch start
        """

        start = time.perf_counter()
        res = streamProcess(request_url)
        finish = time.perf_counter()
        print(f'Finished in {round(finish - start, 2)} second(s)')

        """
        stream data fetch end
        """

        final_ret = {
            "type" : "POST",
            "status" : "Success",
            "url" : request_url,
            "result" : res
        }

        return final_ret
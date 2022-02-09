# -*- coding: UTF-8 -*-
'''
@Project ：youtube_highlight_extract 
@File ：HelloApiHandler.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-07 오후 5:30 
'''

from flask_restful import Api, Resource, reqparse

from api.extract.streamExtract import downloadAudio,downloadVideo, downloadChat
import time

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
        stream data fetch start
        """

        print('start time : ', str(int(time.time())%1000))
        downloadAudio(request_url)
        downloadVideo(request_url)
        url_id = request_url.split("=")[1]
        downloadChat(url_id)
        print('end time : ', str(int(time.time())%1000))

        """
        stream data fetch end
        """

        final_ret = {
            "type" : "POST",
            "status" : "Success",
            "url" : request_url
        }

        return final_ret
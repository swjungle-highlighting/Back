# -*- coding: UTF-8 -*-
'''
@Project ：youtube_highlight_extract 
@File ：HelloApiHandler.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-07 오후 5:30 
'''
import pymysql
from flask_restful import Api, Resource, reqparse

from api.extract.streamExtract import streamProcess
import time

from password import dbpw, dbip

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
        db = pymysql.connect(
            host=dbip,
            port=3306,
            user='root',
            password=dbpw,
            db='highlighting', charset='utf8', autocommit=True  # 실행결과확정
        )

        cursor = db.cursor()
        sql = 'SELECT result FROM youtube WHERE url="' + request_url + '";'
        cursor.execute(sql)

        data = cursor.fetchone()

        if data :
            # if url in db
            result = eval(data[0])

            final_ret = {
                "type": "POST",
                "status": "This is Database",
                "url": request_url,
                "result": result
            }

            db.close()
            print("Success read DB")
            return final_ret

        """
        stream data fetch start
        """

        start = time.perf_counter()
        res = streamProcess(request_url)
        finish = time.perf_counter()
        print(f'Finished in {round(finish - start, 2)} second(s)')

        if res == False:
            return {
                "error" : "id is not valid"
            }

        """
        stream data fetch end
        """

        final_ret = {
            "type" : "POST",
            "status" : "Success insert Database",
            "url" : request_url,
            "result" : res
        }

        """
        insert database
        """
        title = res['title']
        title = title.replace("'", "\\'")
        json_str = '{"audio":'+str(res['audio'])+', "video":'+str(res['video'])+', "chat":'+str(res['chat'])+', "title":'+str('"'+title+'"')+', "thumbnail":'+str('"'+res['thumbnail']+'"')+'}'
        sql = "insert into youtube(url, result) values('"+request_url+"', '"+json_str+"');"
        cursor.execute(sql)
        print("Success insert DB")

        db.close()

        return final_ret
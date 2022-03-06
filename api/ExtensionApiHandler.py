from flask_restful import Api, Resource, reqparse

from password import dbpw, dbip

import json
import pymysql

class ExtensionApiHandler(Resource) :    
    def get(self):
        return {
            'status' : '200',
            'message' : 'Success'
        }

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', type=str)

        args = parser.parse_args()
        print(args)

        request_url = args['url']
        url_id = request_url.split("=")[1]

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

            final_ret = {
                "type": "POST",
                "url": request_url,
                "result": 1,
            }
        else : 
            final_ret = {
                "type": "POST",
                "url": request_url,
                "result": 0,
            }
        db.close()
        return final_ret

# -*- coding: UTF-8 -*-
'''
@Project ：youtube_highlight_extract 
@File ：LogInApiHandler.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-03-06 오후 8:58 
'''

import datetime
import jwt
import pymysql
from flask_restful import Api, Resource, reqparse
from password import dbip, dbpw

class LoginApiHandler(Resource):
    SECRET_KEY = 'TopSecret'
    def get(self):
        return {
            'status' : '200',
            'message' : 'This is get method'
        }

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        parser.add_argument('password', type=str)

        args = parser.parse_args()

        request_id = args['id']
        request_password = args['password']


        db = pymysql.connect(
            host=dbip,
            port=3306,
            user='root',
            password=dbpw,
            db='highlighting', charset='utf8', autocommit=True  # 실행결과확정
        )

        cursor = db.cursor()
        sql = 'SELECT id, password, name FROM user WHERE id="' + request_id + '";'
        cursor.execute(sql)
        data = cursor.fetchone()

        final_ret = ''
        name = ''

        if data:
            db_password = data[1]
            name = data[2]
            if request_password == db_password:

                payload = {
                    'ID': request_id,
                    'NAME': name,
                    'EXP': str(datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 60 * 24))
                }
                token = jwt.encode(payload, self.SECRET_KEY, algorithm='HS256')

                final_ret = {
                    'status': '200',
                    'url': 'login',
                    'token': token,
                    'message': "success log in",
                }

            else:
                final_ret = {
                    'status': '400',
                    'url': 'login',
                    'message': "password don't match",
                }
        else:
            final_ret = {
                'status': '400',
                'url': 'login',
                'message': "id don't exist",
            }

        db.close()
        return final_ret
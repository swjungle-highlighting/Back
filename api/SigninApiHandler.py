# -*- coding: UTF-8 -*-
'''
@Project ：youtube_highlight_extract 
@File ：SignInApiHandler.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-03-06 오후 8:58 
'''
import pymysql
from flask_restful import Api, Resource, reqparse
from password import dbip, dbpw

class SigninApiHandler(Resource):
    def get(self):
        return {
            'status' : '200',
            'message' : 'This is get method'
        }

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('passwordChk', type=str)
        parser.add_argument('name', type=str)

        args = parser.parse_args()

        request_id = args['id']
        request_password = args['password']
        request_passwordChk = args['passwordChk']
        request_name = args['name']

        db = pymysql.connect(
            host=dbip,
            port=3306,
            user='root',
            password=dbpw,
            db='highlighting', charset='utf8', autocommit=True  # 실행결과확정
        )

        cursor = db.cursor()
        sql = 'SELECT id FROM user WHERE id="' + request_id + '";'
        cursor.execute(sql)
        data = cursor.fetchone()

        final_ret = ''

        if data :
            final_ret = {
                'status': '400',
                'url' : 'signin',
                'message': 'id is already exist',
            }
        else:
            sql = "insert into user(id, password, name) values('"+request_id+"', '"+request_password+"', '"+request_name+"');"
            print(sql)
            cursor.execute(sql)

            final_ret = {
                'status': '200',
                'url': 'signin',
                'message': 'success insert user in db',
            }

        db.close()
        return final_ret
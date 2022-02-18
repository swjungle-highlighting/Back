# -*- coding: UTF-8 -*-
'''
@Project ：swfinal 
@File ：db.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-12 오후 5:55 
'''

from password import dbpw,dbip
import pymysql

db = pymysql.connect(
    host=dbip,
    port=3306,
    user='root',
    password=dbpw,
    db='highlighting', charset='utf8', autocommit=True # 실행결과확정
)

cursor = db.cursor()

"""
    delete
"""
sql = "delete from youtube;"
cursor.execute(sql)


db.close()
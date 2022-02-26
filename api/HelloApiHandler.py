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



digit = ['0','1','2','3','4','5','6','7','8','9']
def _cut_time_and_messageset(line) :
    i = 0
    elapsetime = ''
    while line[i] in digit :
        elapsetime += line[i]
        i += 1
    return int(elapsetime), line[i+1:]

def _str_to_list(message) :
    return message[2:len(message)-3].split("', '")

## 이 함수 인풋값에 '5c3wiaogv-Q'같은 url id 입력하면 됨
def return_MessageSet(URL_ID) :
    MessageSet = {}
    chat_file = open('./chat_storage/'+URL_ID+'.txt', "r", encoding = 'UTF8')
    target = chat_file.readline().rstrip()
    i = 0
    while target :
        second, message = _cut_time_and_messageset(target)
        MessageSet[second] = _str_to_list(message)
        i += 1
        target = chat_file.readline()
    chat_file.close()
    return MessageSet


class HelloApiHandler(Resource):
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
            url_id = request_url.split("=")[1]
            chat = result['chat']
            chatSet = return_MessageSet(url_id)
            chat = [chat[0]] + [chatSet] + [chat[1]]
            result['chat'] =chat

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
        chat = res['chat']
        chat = [chat[0] ]+[chat[2]]
        json_str = '{"audio":'+str(res['audio'])+', "video":'+str(res['video'])+', "chat":'+str(chat)+', "title":'+str('"'+title+'"')+', "thumbnail":'+str('"'+res['thumbnail']+'"')+', "duration":'+str('"'+str(res['duration'])+'"')+'}'
        sql = "insert into youtube(url, result) values('"+request_url+"', '"+json_str+"');"
        cursor.execute(sql)
        print("Success insert DB")

        db.close()

        return final_ret
# -*- coding: UTF-8 -*-
'''
@Project ：youtube_highlight_extract 
@File ：app.py.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-07 오후 5:28 
'''

from flask import Flask, send_from_directory, send_file
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from api.HelloApiHandler import HelloApiHandler
from api.KeywordsApiHandler import KeywordsApiHandler
from api.DownloadApiHandler import DownloadApiHandler

from api.download_logic.do_logic import create_cutTool, delete_cutTool

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app)
api = Api(app)

@app.route("/", defaults={'path' : ''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(HelloApiHandler, '/flask/hello')
api.add_resource(KeywordsApiHandler, '/flask/keywords')
api.add_resource(DownloadApiHandler, '/flask/download')

@app.route("/downloadpath")
def download() :
    return send_file("HIGHLIGHTING.zip")
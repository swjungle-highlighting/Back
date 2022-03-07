# -*- coding: UTF-8 -*-
'''
@Project ：youtube_highlight_extract 
@File ：app.py.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-07 오후 5:28 
'''

from flask import Flask, request, send_from_directory, send_file, render_template
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from api.HelloApiHandler import HelloApiHandler
from api.KeywordsApiHandler import KeywordsApiHandler
from api.BookMarkerApiHandler import BookMarkerApiHandler
from api.DownloadApiHandler import DownloadApiHandler
from api.ExtensionApiHandler import ExtensionApiHandler
from api.LoginApiHandler import LoginApiHandler
from api.SigninApiHandler import SigninApiHandler
from api.OauthApiHandler import OauthApiHandler


app = Flask(__name__, static_url_path='', static_folder='./static')
CORS(app)
api = Api(app)

@app.route("/", defaults={'path' : ''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(HelloApiHandler, '/flask/hello')
api.add_resource(KeywordsApiHandler, '/flask/keywords')
api.add_resource(BookMarkerApiHandler, '/bookmarker')
api.add_resource(DownloadApiHandler, '/flask/download')
api.add_resource(ExtensionApiHandler, '/extension')

api.add_resource(LoginApiHandler, '/logIn')
api.add_resource(SigninApiHandler, '/signIn')
api.add_resource(OauthApiHandler, '/OAuth')

@app.route("/downloadpath", methods = ['GET', 'POST'])
def download() : 
    if request.method == 'GET' :
        return send_file("HIGHLIGHTING.zip")

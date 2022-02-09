# -*- coding: UTF-8 -*-
'''
@Project ：youtube_highlight_extract 
@File ：videoProcess.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-09 오후 6:38 
'''

import os

def videoProcess(url_id):
    print('video ' + url_id)

    """"""

    folder = os.getcwd()
    target = ''
    for filename in os.listdir(folder+'/api/video/'):
        if url_id in filename:
            target = filename
    print('video target : ' + target)

    """"""
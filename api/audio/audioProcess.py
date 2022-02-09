# -*- coding: UTF-8 -*-
'''
@Project ：youtube_highlight_extract 
@File ：audioProcess.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-09 오후 6:37 
'''

import os

def audioProcess(url_id):
    print('audio ' + url_id)

    """"""

    folder = os.getcwd()
    target = ''
    for filename in os.listdir(folder+'/api/audio/'):
        if url_id in filename:
            target = filename
    print('audio target : ' + target)

    """"""
# -*- coding: UTF-8 -*-
'''
@Project ：youtube_highlight_extract 
@File ：streamExtract.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-09 오후 12:30 
'''
import os

import yt_dlp

from api.audio.audioProcess import audioProcess
from api.video.videoProcess import videoProcess
from api.chat.chatProcess import chatProcess

opts = {
    'ignoreerrors' : True,
    'nooverwrites' : True,
    'format' : 'worstvideo[height<=144]+worstaudio/worst[height<=144]/worst',
    'outtmpl' : './api/extract/%(id)s.%(ext)s',
}

def streamProcess(url):
    print('::stream::')
    url_id = url.split("=")[1]

    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])
        info_dict = ydl.extract_info(url, download=False)
        duration = info_dict.get('duration', None)

    audio= audioProcess(url_id)
    video= videoProcess(url_id)
    chat= chatProcess(url_id, duration)

    folder = os.getcwd()
    target = ''
    for filename in os.listdir(folder + '/api/extract/'):
        if url_id in filename:
            target = filename

    os.remove(folder + '/api/extract/' + target)
    print('delete stream target!!')

    return {'audio' : audio,
            'video' : video,
            'chat' : chat}

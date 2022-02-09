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

audio_opts = {
    'ignoreerrors' : True,
    'nooverwrites' : True,
    'format' : 'worstaudio',
    'outtmpl' : './api/audio/%(id)s.%(ext)s',
}

video_opts = {
    'ignoreerrors' : True,
    'nooverwrites' : True,
    'format' : 'worstvideo',
    'outtmpl' : './api/video/%(id)s.%(ext)s',
}

def downloadAudio(url):
    print('::audio::')
    with yt_dlp.YoutubeDL(audio_opts) as ydl:
        ydl.download([url])
        info_dict = ydl.extract_info(url, download=False)
        # print(info_dict.get('id', None))
        audioProcess(info_dict.get('id', None))

def downloadVideo(url):
    print('::video::')
    with yt_dlp.YoutubeDL(video_opts) as ydl:
        ydl.download([url])
        info_dict = ydl.extract_info(url, download=False)
        # print(info_dict.get('id', None))
        videoProcess(info_dict.get('id', None))

def downloadChat(url_id):
    print('::chat::')
    chatProcess(url_id)

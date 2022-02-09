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

# def my_hook(d):
#     if d['status'] == 'finished':
#         print("Done downloading, now converting ... ")

audio_opts = {
    'ignoreerrors' : True,
    'nooverwrites' : True,
    'format' : 'worstaudio',
    'outtmpl' : './api/audio/%(title)s.%(ext)s',
}

video_opts = {
    'ignoreerrors' : True,
    'nooverwrites' : True,
    'format' : 'worstvideo',
    'outtmpl' : './api/video/%(title)s.%(ext)s',
}

def downloadAudio(url):
    print('audio', os.path.realpath(__file__))
    with yt_dlp.YoutubeDL(audio_opts) as ydl:
        ydl.download([url])

def downloadVideo(url):
    print('video')
    with yt_dlp.YoutubeDL(video_opts) as ydl:
        ydl.download([url])
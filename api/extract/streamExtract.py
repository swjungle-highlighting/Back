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

def _sec_to_str(sec) :
    t = []
    t.append(sec %60)
    t.append((sec %3600 -t[0])//60)
    t.append(sec //3600)
    for i in range(3) :
        if t[i] < 10 :
            t[i] = '0'+str(t[i])
        else :
            t[i] = str(t[i])
    return t[2]+':'+t[1]+':'+t[0]

CUT_RANGE = 600
def _do_subprocess(input_file, duration, index, audio, video) :
    output_file = str(index) + input_file
    start = index * CUT_RANGE
    end = min(duration, (index+1) * CUT_RANGE)
    ffmpeg_call = ["ffmpeg -ss", _sec_to_str(start), "-to", _sec_to_str(end),  "-i", input_file, "-c copy", output_file]
    os.system(" ".join(ffmpeg_call))
    audio += audioProcess(output_file)
    video += videoProcess(output_file)
    os.remove(os.getcwd() + "/" + output_file)

opts = {
    'ignoreerrors' : True,
    'nooverwrites' : True,
    'format' : 'worstvideo[height<=144]+worstaudio/worst[height<=144]/worst',
    'outtmpl' : './%(id)s.%(ext)s',
}

def streamProcess(url):
    print('::stream::')
    url_id = url.split("=")[1]

    if len(url_id) != 11:
        return False

    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])
        info_dict = ydl.extract_info(url, download=False)
        duration = info_dict.get('duration', None)
        title = info_dict.get('title')
        thumbnail = info_dict.get('thumbnail')

    input_file = url_id+'.mp4'
    audio= []
    video= []
    index = 0
    while index <= duration //CUT_RANGE :
        _do_subprocess(input_file, duration, index, audio, video)
        index += 1

    chat = chatProcess(url_id, duration)

    folder = os.getcwd()
    target = ''
    for filename in os.listdir(folder + '/'):
        if url_id in filename:
            target = filename

    os.remove(folder + '/' + target)
    print('delete stream target!!')
    print(len(video), len(audio), len(chat[0]))

    return {
            'audio' : audio,
            'video' : video,
            'chat' : chat,
            'title' : title,
            'thumbnail' : thumbnail,
            'duration' : duration
            }
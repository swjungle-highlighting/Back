# -*- coding: UTF-8 -*-
'''
@Project ：youtube_highlight_extract 
@File ：videoProcess.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-09 오후 6:38 
'''

import os
import ffmpeg
import numpy

W, H = 128, 72
FPS = 10

def videoProcess(url_id):
    print("########################################################")
    print('video ' + url_id)
    print("########################################################")
    """"""

    folder = os.getcwd()
    target = ''
    for filename in os.listdir(folder+'/api/extract/'):
        if url_id in filename:
            target = filename

    out, err = (
        ffmpeg
            .input(folder+'/api/extract/'+target)
            .filter('fps', fps=FPS, round='up')
            .filter('scale', w=W, h=H)
            .output('pipe:', format='rawvideo', pix_fmt='rgb24')
            .run(capture_stdout=True)
    )
    frames = (
        numpy
            .frombuffer(out, numpy.uint8)
            .reshape([-1, H, W, 3])
    )

    diff = []
    before = 0
    for i in range(len(frames)):
        now = int(frames[i].sum())
        diff.append(abs(now - before) // 768)
        before = now

    VideoDATA_3600perHOUR = []
    summ = 0
    for i in range(len(diff)):
        if not i %FPS:
            VideoDATA_3600perHOUR.append(summ)
            summ = 0
        summ += diff[i]

    return VideoDATA_3600perHOUR

    """"""
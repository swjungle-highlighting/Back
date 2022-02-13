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

    VideoDATA_3600perHOUR = []

    summ, before = 0, numpy.array([])
    for i in range(1, len(frames)) : 
        if not i %FPS : 
            VideoDATA_3600perHOUR.append(summ)
            summ = 0
        now = frames[i]
        summ += abs(int(now.sum()) - int(before.sum()))
        before = now
    return VideoDATA_3600perHOUR

    """"""
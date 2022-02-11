# -*- coding: UTF-8 -*-
'''
@Project ：youtube_highlight_extract 
@File ：audioProcess.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-09 오후 6:37 
'''

import os
import numpy
import ffmpeg

def audioProcess(url_id):
    print('audio ' + url_id)

    """"""

    folder = os.getcwd()
    target = ''
    for filename in os.listdir(folder+'/api/extract/'):
        if url_id in filename:
            target = filename
    print('audio target : ' + target)

    SAMPLERATE = 11050

    out, err = (
        ffmpeg
            .input(folder+'/api/extract/'+target)
            .output('-', format='f32le', acodec='pcm_f32le', ac=1, ar=str(SAMPLERATE))
            .run(capture_stdout=True)
    )

    amplitudes = numpy.frombuffer(out, numpy.float32)

    cal = []
    summ = 0
    for i in range(len(amplitudes)):
        if not i % SAMPLERATE:
            cal.append(summ)
            summ = 0
        summ += abs(amplitudes[i])

    return cal

    # os.remove(folder+'/api/audio/'+target)
    # print('delete audio target!!')
    """"""
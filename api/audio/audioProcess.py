# -*- coding: UTF-8 -*-
'''
@Project ：youtube_highlight_extract 
@File ：audioProcess.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-09 오후 6:37 
'''

import os
import numpy as np
import librosa

def audioProcess(url_id):
    print('audio ' + url_id)

    """"""

    folder = os.getcwd()
    target = ''
    for filename in os.listdir(folder+'/api/audio/'):
        if url_id in filename:
            target = filename
    print('audio target : ' + target)

    wav, sr = librosa.load(target)

    n_fft = 2048
    hop_length = 512
    stft = librosa.stft(wav, n_fft=n_fft, hop_length=hop_length)

    spectrogram = np.abs(stft)
    log_spectrogram = librosa.amplitude_to_db(spectrogram)
    n = np.array(log_spectrogram)

    os.remove(folder+'/api/audio/'+target)
    print('delete audio target!!')
    """"""
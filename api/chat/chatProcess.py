# -*- coding: UTF-8 -*-
'''
@Project ：youtube_highlight_extract 
@File ：chatProcess.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-09 오후 6:38 
'''

import pytchat

def chatProcess(url_id, duration):
    print("########################################################")
    print('chat : ' + url_id)
    print("########################################################")
    """"""

    maxminute = (duration//60)+1
    Distribution = [0 for i in range(maxminute + 1)]

    chatset = pytchat.create(video_id=url_id, interruptable=False)

    while chatset.is_alive():
        data = chatset.get()
        items = data.items
        for item in items : 
            t = item.elapsedTime
            lent = len(t)
            if lent == 4 : 
                hh = 0
                mm = int(t[0])
            elif lent == 5 :
                hh = 0
                mm = max(0, int(t[0:2]))
            elif lent == 7 : 
                hh = int(t[0])
                mm = int(t[2:4])
            else : 
                hh, mm = 0, 0
            minute = hh*60 + mm + 1
            if minute > maxminute : 
                break
            Distribution[minute] += 1
    
    return Distribution

    """"""
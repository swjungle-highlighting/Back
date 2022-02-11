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
    print('chat : ' + url_id)

    """"""

    ####### 영상 길이 동적으로
    maxminute = (duration//60)+1  # 10시간이면 충분하겠지
    Distribution = [0 for i in range(maxminute + 1)]

    chatset = pytchat.create(video_id=url_id, interruptable=False)

    data = chatset.get()

    while chatset.is_alive():
        data = chatset.get()
        items = data.items
        len_items = len(items)
        if len_items:
            t = items[0].elapsedTime
            lent = len(t)
            if lent == 4:
                hh = 0
                mm = int(t[0])
            elif lent == 5:
                hh = 0
                mm = int(t[0:2])
            elif lent == 7:
                hh = int(t[0])
                mm = int(t[2:4])
            minute = hh * 60 + mm
            # 혹시 최대 range 이상의 긴 영상이 제공될 경우 index over 방지
            if minute > maxminute:
                break
            Distribution[minute] += len_items

    return Distribution

    """"""
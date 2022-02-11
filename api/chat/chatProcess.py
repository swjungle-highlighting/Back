# -*- coding: UTF-8 -*-
'''
@Project ：youtube_highlight_extract 
@File ：chatProcess.py
@IDE  ：PyCharm 
@Author ： Hwang
@Date ：2022-02-09 오후 6:38 
'''

import pytchat

def chatProcess(url_id):
    print('chat : ' + url_id)

    """"""

    chatset = pytchat.create(video_id=url_id, interruptable=False)
    while chatset.is_alive():
        try:
            data = chatset.get()
            items = data.items
            # for c in items:
            #     print(c)

        except KeyboardInterrupt:
            chatset.terminate()
            break

    """"""
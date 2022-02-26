import os

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

def cut_video(input_file, index, start, end) :
    output_file = 'HIGHLIGHT_' + str(index) + '_' + input_file
    input_path = '"' + os.getcwd() + '/../' + input_file + '"'
    output_path = '"' + os.getcwd() + '/../' + output_file + '"'
    ffmpeg_call = ["ffmpeg -ss", _sec_to_str(start), "-to", _sec_to_str(end),  "-i", input_path, "-c copy", output_path]
    os.system(" ".join(ffmpeg_call))

input_file = input('분할할 영상파일의 이름을 입력하세요 : ')

chat_file = open('./user_query.txt', "r", encoding = 'UTF8')
target = chat_file.readline().rstrip()
index = 1
while target : 
    start, end = map(int, target.split())
    cut_video(input_file, index, start, end)
    index += 1
    target = chat_file.readline()
chat_file.close()
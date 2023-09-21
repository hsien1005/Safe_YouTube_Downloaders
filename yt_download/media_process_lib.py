from pytube import YouTube
import os
import ffmpeg
import subprocess
import librosa
#import numpy as np
#import matplotlib.pyplot as plt


#from test import onProgress
def onProgress(stream, chunk, remains):
    total = stream.filesize
    percent = (total-remains) / total * 100
    print('下載中… {:05.2f}%'.format(percent), end='\r')

# pytube下載一個影片
def downloadYT(url,path = os.getcwd(),filename=""):
    yt = YouTube(url)
    # yt.streams.first().download()
    if filename: 
        filename = filename+'.mp4' if not filename.endswith('.mp4') else filename
    else:
        filename = yt.streams.get_highest_resolution().default_filename

    yt.streams.get_highest_resolution().download(path,filename=filename)

    return filename
    
# 音畫合成  # 請用cmd/PS執行
def combine(inputvideo,inputaudio,outputvideo):
    # outputvideo = "合成" + outputvideoname
    command = 'ffmpeg -i {inputvideo} -i {inputaudio} -map 0:v -map 1:a -c copy -y {outputvideo}'.format(inputvideo=inputvideo,inputaudio=inputaudio,outputvideo=outputvideo)
    subprocess.call(command,shell=True)
  
"""
# 抽取audio
def getaudio(inputfilename):
  stream = ffmpeg.input(inputfilename)
  return stream.audio
"""
# 存成mp3  
def mp4_to_mp3(inputfilename,outputfilename,path = os.getcwd()):
    stream = ffmpeg.input(os.path.join(path,inputfilename))
    audio = stream.audio
    out = ffmpeg.output(audio,os.path.join(path,outputfilename))
    out.run()
  
def batch_to_mp3(path = os.getcwd()):
    mp3,mp4 = get_all_file(path)
    for file in mp4:
        mp4_to_mp3(file, file.split(".")[0] +'.mp3',path)


# 調整mp3音量
def adjaudio(file,multiple,path = os.getcwd()):  # mp3 mp4通用，output only audio
    #filestyle = file.split(".")[1] # check mp3 mp4
    newfile = "audio{:.2f}x".format(multiple)+file  # 新檔名；倍數x原filename  (不能同檔名)
    
    stream = ffmpeg.input(os.path.join(path,file))
    stream = ffmpeg.filter(stream, 'volume', volume=multiple)
    stream = ffmpeg.output(stream, os.path.join(path,newfile))
    ffmpeg.run(stream) 
    return newfile


# 調整mp4音量
def adj_video_vol(file,multiple,path = os.getcwd()):
    outputvideoname = "{:.2f}x".format(multiple)+file
    
    stream = ffmpeg.input(os.path.join(path,file))
    audio = stream.audio
    audio = ffmpeg.filter(stream, 'volume', volume=multiple)
    out = ffmpeg.output(audio, stream.video, os.path.join(path,outputvideoname))
    ffmpeg.run(out)
    #combine(inputvideo,adjaudio(inputvideo,multiple),outputvideoname)
    return outputvideoname


#########
def get_all_file(path):
    files = os.listdir(path)
    mp3 = []
    mp4 = []
    for file in files:
        if file.endswith('.mp3'): # 以.mp3為副檔名
            mp3.append(file)    # 加入串列
        if file.endswith('.mp4'): # 以.mp4為副檔名
            mp4.append(file)    # 加入串列
    return mp3,mp4

# 平均 mp3 音量
def batch_adj_mp3(path = os.getcwd()):
    if path=='':
        path = os.getcwd()
        
    mp3,mp4 = get_all_file(path)
    
    # 每個mp3音檔的平均音量
    from numpy.lib.function_base import average
    avg_mp3 = []
    for i in range(len(mp3)):
        a, f = librosa.load(os.path.join(path,mp3[i])) # (os.path.join(path,file))
        avg_mp3.append(average(abs(a)))
    print(avg_mp3)
    
    # 將資料夾中所有檔案音量調整一致
    avgvol = average(avg_mp3)
    adj_audio_filename = []
    for i in range(len(mp3)):
        multiple = round(avgvol/avg_mp3[i],2)
        print(multiple)
        adj_audio_filename.append(adjaudio(mp3[i],multiple,path))
    print(adj_audio_filename)
        
# 平均 mp4 音量
def batch_adj_mp4(path = os.getcwd()):
    if path=='':
        path = os.getcwd()
        
    mp3,mp4 = get_all_file(path)
    
    # 每個mp4音檔的平均音量
    from numpy.lib.function_base import average
    avg_mp4 = []
    for i in range(len(mp4)):
        a, f = librosa.load(os.path.join(path,mp4[i]))
        avg_mp4.append(average(abs(a)))
    print(avg_mp4)
    
    # 將資料夾中所有檔案音量調整一致
    avgvol = average(avg_mp4)
    adj_audio_filename = []
    for i in range(len(mp4)):
        multiple = round(avgvol/avg_mp4[i],2)
        print(multiple)
        adj_audio_filename.append(adj_video_vol(mp4[i],multiple,path))
    print(adj_audio_filename)
        
        
        
""" -----------------------------------"""


if __name__ == '__main__':
    #main()
    path = 'C:\\Users\\tin\\Desktop\\python' # os.getcwd()  
    # 下載影片
    url = 'https://www.youtube.com/watch?v=iWDmqmZ2ZXA'    # piano
    # https://www.youtube.com/watch?v=0ktoTdrxMD4
    filename = "pianotest"
    #title = downloadYT(url)
    filename = downloadYT(url,path,filename)
    # 轉出mp3
    filename_of_mp3 = filename.split(".")[0] +'.mp3'
    mp4_to_mp3(filename,filename_of_mp3,path)
    
    # adj
    get_all_file(path)
        
    # 調整mp4音量
    adj_video_vol(filename,5)
    
    


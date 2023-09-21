from media_process_lib import *
from download_process_lib import *
import tkinter as tk
from tkinter import ttk
import os
win = tk.Tk()                         # 建立主視窗物件
win.configure(bg='black')
win.geometry('640x480')                # 設定主視窗預設尺寸為640x480
win.resizable(True,True)             # 設定主視窗的寬跟高皆可縮放
win.title('YouTube Video Downloader')  # 設定主視窗標題
from PIL import Image
from PIL import ImageTk
#設定網址輸入區域
input_frm = tk.Frame(win, width=640, height=50,bg='black')

input_frm.pack()
#設定提示文字
lb = tk.Label(input_frm, text='Type a link like a video or a playlist',fg='black')
lb.place(rely=0.2, relx=0.5, anchor='center')


#設定輸入框
input_url = tk.StringVar()     # 取得輸入的網址
input_et = tk.Entry(input_frm, textvariable=input_url, width=40)
input_et.place(rely=0.75, relx=0.4, anchor='center')
input_path = tk.StringVar()  # 取得輸入的路徑
input_name = tk.StringVar()

input_path_mp3 = tk.StringVar()
input_path_mp4 = tk.StringVar()
input_filename_mp3 = tk.StringVar()
input_filename_mp4 = tk.StringVar()
input_multi_mp3 = tk.StringVar()
input_multi_mp4 = tk.StringVar()
input_average_mp3 = tk.StringVar()
input_average_mp4 = tk.StringVar()
input_mp4_mp3=tk.StringVar()
path_mp4_to_mp3 = tk.StringVar()


#設定按鈕
def path_click():   # 按鈕的函式
    print(input_path.get())
def name_click():   # 按鈕的函式
    print(input_name.get())
    
    
  # in change  
def average_mp3():
    print("start change.")
    batch_adj_mp3(input_average_mp3.get())
def average_mp4():    
    print("start change.")
    batch_adj_mp4(input_average_mp4.get())
    
def set_filename_mp3():     #change_mp3_vol
    print(input_path_mp3.get(),input_filename_mp3.get())
    filename = input_filename_mp3.get()
    if not filename.endswith('.mp3'):
        filename = filename+'.mp3'
    adjaudio(filename,int(input_multi_mp3.get()),input_path_mp3.get())
def set_filename_mp4():     #change_mp4_vol
    print(input_filename_mp4.get())
    filename = input_filename_mp4.get()
    if not filename.endswith('.mp4'):
        filename = filename+'.mp4'
    adj_video_vol(filename,int(input_multi_mp4.get()),input_path_mp4.get())
    
def change_mp4_to_mp3():
    print(input_mp4_mp3)
    if input_mp4_mp3.get()=='':
        batch_to_mp3(path_mp4_to_mp3.get())
    else:
        filename = input_mp4_mp3.get()
        if not filename.endswith('.mp4'):
            filename = filename+'.mp4'    
        filename_of_mp3 = filename.split(".")[0] +'.mp3'
        mp4_to_mp3(filename,filename_of_mp3,path_mp4_to_mp3.get())
    
    

    
# 設定按鈕
def to_mp3():   # Transform mp3
    print("mp3")
    print(input_url.get(),input_name.get())
    inputfilename = downloadYT(input_url.get(),filename=input_name.get(),path=input_path.get())  # 是否要刪掉mp4？ os.remove(os.path.join(path,inputfilename))
    filename_of_mp3 = inputfilename.split(".")[0] +'.mp3'
    mp4_to_mp3(inputfilename,filename_of_mp3,input_path.get())
    listbox.insert(tk.END, '{}下載完成.....'.format(filename_of_mp3))

def to_mp4():   # download mp4
    print("mp4")
    print(input_url.get(),input_name.get())
    filename = downloadYT(input_url.get(),filename=input_name.get(),path=input_path.get())
    listbox.insert(tk.END, '{}下載完成.....'.format(filename))
    
def download_list(): # Download_playlist
    newWindow1 = tk.Toplevel(win)
    newWindow1.configure(bg='black')
    newWindow1.geometry('200x100')
    def button_event():
       # print(mycombobox.current(), mycombobox.get())
         print(mycombobox.current())
         #print(type(mycombobox.get()))
         buttonText.set('enter:' + ', ' + mycombobox.get())
         
         num = download_playlist(input_url.get(),mycombobox.current()+1,path=input_path.get()) # high=0+1,low=1+1
         listbox.insert(tk.END, '已下載{}個影片.....'.format(num))
        
    comboboxList = ['High','Low']
    mycombobox = ttk.Combobox(newWindow1, state='readonly')
    mycombobox['values'] = comboboxList
    mycombobox.pack(pady=10)
    mycombobox.current(0)
    buttonText = tk.StringVar()
    buttonText.set('button')
    tk.Button(newWindow1, textvariable=buttonText, command=button_event).pack()
    
def change():
    newWindow = tk.Toplevel(win)
    newWindow.configure(bg='black')
    # 設定path輸入區域
    input_frm2 = tk.Frame(newWindow, width=640, height=350, bg='black')

    input_frm2.pack()
    # 設定平均mp3音量按鈕
    input_aver_mp3 = tk.Entry(input_frm2, textvariable=input_average_mp3, width=40)
    input_aver_mp3.place(rely=0.1, relx=0.43, anchor='center')
    btn_average_mp3 = tk.Button(input_frm2, text='Average all mp3 vol in the folder', command=average_mp3,
                           bg='orange', fg='black')
    btn_average_mp3.place(rely=0.1, relx=0.81, anchor='center')
    # 設定平均mp4音量按鈕
    input_aver_mp4 = tk.Entry(input_frm2, textvariable=input_average_mp4, width=40)
    input_aver_mp4.place(rely=0.3, relx=0.43, anchor='center')
    btn_average_mp4 = tk.Button(input_frm2, text='Average all mp4 vol in the folder', command=average_mp4,
                                bg='orange', fg='black')
    btn_average_mp4.place(rely=0.3, relx=0.81, anchor='center')

    # 設定提示文字
    lbnam = tk.Label(input_frm2, text='change mp3 volumn', fg='black')
    lbnam.place(rely=0.42, relx=0.5, anchor='center')

    # 設定輸入框
    input_pnam_mp3 = tk.Entry(input_frm2, textvariable=input_path_mp3, width=40)
    input_pnam_mp3.place(rely=0.5, relx=0.35, anchor='center')
    input_fnam_mp3 = tk.Entry(input_frm2, textvariable=input_filename_mp3, width=20)
    input_fnam_mp3.place(rely=0.5, relx=0.7, anchor='center')
    input_mul_mp3 = tk.Entry(input_frm2, textvariable=input_multi_mp3, width=2)
    input_mul_mp3.place(rely=0.5, relx=0.85, anchor='center')
    ftn1 = tk.Button(input_frm2, text='enter', command=set_filename_mp3,
                    bg='orange', fg='Black')
    ftn1.place(rely=0.5, relx=0.92, anchor='center')

    # 設定提示文字
    lbnam = tk.Label(input_frm2, text='change mp4 volumn', fg='black')
    lbnam.place(rely=0.62, relx=0.5, anchor='center')
    # 設定輸入框
    input_pnam_mp4 = tk.Entry(input_frm2, textvariable=input_path_mp4, width=40)
    input_pnam_mp4.place(rely=0.7, relx=0.35, anchor='center')
    input_fnam_mp4 = tk.Entry(input_frm2, textvariable=input_filename_mp4, width=20)
    input_fnam_mp4.place(rely=0.7, relx=0.7, anchor='center')
    input_mul_mp4 = tk.Entry(input_frm2, textvariable=input_multi_mp4, width=2)
    input_mul_mp4.place(rely=0.7, relx=0.85, anchor='center')
    ftn2 = tk.Button(input_frm2, text='enter', command=set_filename_mp4,
                    bg='orange', fg='Black')
    ftn2.place(rely=0.7, relx=0.92, anchor='center')
    
    #mp4 to mp3
    lbnam = tk.Label(input_frm2, text='mp4 to mp3', fg='black')
    lbnam.place(rely=0.82, relx=0.5, anchor='center')
    input_path_mp4_to_mp3 = tk.Entry(input_frm2, textvariable=path_mp4_to_mp3, width=40)
    input_path_mp4_to_mp3 .place(rely=0.9, relx=0.35, anchor='center')
    input_mp4_to_mp3 = tk.Entry(input_frm2, textvariable=input_mp4_mp3, width=20)
    input_mp4_to_mp3.place(rely=0.9, relx=0.7, anchor='center')
    m4to3 = tk.Button(input_frm2, text='enter', command=change_mp4_to_mp3,
                     bg='orange', fg='Black')
    m4to3.place(rely=0.9, relx=0.89, anchor='center')
    
    
def btn_click():   # 按鈕的函式

    newWindow = tk.Toplevel(win)
    newWindow.configure(bg='black')
    # 設定path輸入區域
    input_frm1 = tk.Frame(newWindow, width=640, height=50,bg='black')

    input_frm1.pack()
    # 設定提示文字
    lb = tk.Label(input_frm1, text='Type a path you want', fg='black')
    lb.place(rely=0.3, relx=0.5, anchor='center')

    # 設定輸入框

    input_ep = tk.Entry(input_frm1, textvariable=input_path, width=60)
    input_ep.place(rely=0.75, relx=0.5, anchor='center')
    ptn = tk.Button(input_frm1, text='enter', command=path_click,
                    bg='orange', fg='Black')
    ptn.place(rely=0.75, relx=0.9, anchor='center')
    input_nf = tk.Frame(newWindow, width=640, height=50,bg='black')

    input_nf.pack()
    # 設定提示文字
    lbnam = tk.Label(input_nf, text='Type a name you want', fg='black')
    lbnam.place(rely=0.3, relx=0.5, anchor='center')

    # 設定輸入框

    input_nam = tk.Entry(input_nf, textvariable=input_name, width=60)
    input_nam.place(rely=0.75, relx=0.5, anchor='center')
    ntn = tk.Button(input_nf, text='enter', command=name_click,
                    bg='orange', fg='Black')
    ntn.place(rely=0.75, relx=0.9, anchor='center')




btn = tk.Button(input_frm, text='click here to change path or filename', command = btn_click,
                bg='orange', fg='Black')
btn.place(rely=0.75, relx=0.8, anchor='center')
btn_mp3 = tk.Button(win, text='Transform_mp3', command = to_mp3,
                bg='orange', fg='Black')
btn_mp3.place(rely=0.75, relx=0.2, anchor='center')
btn_mp4 = tk.Button(win, text='Download_mp4', command = to_mp4,
                bg='orange', fg='black')
btn_mp4.place(rely=0.75, relx=0.4, anchor='center')
list = tk.Button(win, text='Download_playlist', command = download_list,
                bg='orange', fg='black')
list.place(rely=0.75, relx=0.6, anchor='center')
btn_change = tk.Button(win, text='change', command = change,
                bg='orange', fg='black')
btn_change.place(rely=0.75, relx=0.8, anchor='center')

#下載清單區域
dl_frm = tk.Frame(win, width=640, height=280,bg='black')
dl_frm.pack()
#設定提示文字
lb = tk.Label(dl_frm, text='Download list',fg='black')
lb.place(rely=0.1, relx=0.5, anchor='center')
#設定顯示清單
listbox = tk.Listbox(dl_frm, width=65, height=15)
listbox.place(rely=0.6, relx=0.5, anchor='center')
#設定捲軸
sbar = tk.Scrollbar(dl_frm)
sbar.place(rely=0.6, relx=0.87, anchor='center', relheight=0.75)
#連結清單和捲軸
listbox.config(yscrollcommand = sbar.set)
sbar.config(command = listbox.yview)
#啟動主視窗
win.mainloop()
#新增分頁





win.mainloop()


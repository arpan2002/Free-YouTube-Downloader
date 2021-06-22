from tkinter import *
import tkinter
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("Arpan_Youtube Video Downloader")
root.wm_iconbitmap('icon.ico')

Label(root,text = 'Youtube Video Downloader', font = 'arial 20 bold').pack()
link = StringVar()

Label (root, text ='Paste Link Here:', font = 'arial 15 bold').place(x= 160, y = 50)
link_enter = Entry(root, width = 70, textvariable=link).place(x = 32, y = 90)

#########Creating Function#########

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text= 'DOWNLOADED', font= 'arial 15').place(x= 180, y =210)
    
Button(root,text = 'DOWNLOADED', font = 'arial 15 bold', bg = 'red',padx = 2, command = Downloader).place(x = 180, y = 150)  

root.mainloop()
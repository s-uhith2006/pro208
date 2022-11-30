from cProfile import label
import chunk
from email import message
from lib2to3.pgen2.token import NAME
from msilib.schema import ListBox
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog 
import ftplib
from ftplib import FTP
import os
import ntpath
import time

IP_ADDRESS='127.0.0.1'
PORT=8080
SERVER=None


def musicWindow():
    window=Tk()
    window.title('music window')
    window.geometry("300x300")
    window.configure(bg="lightskyblue")

    namelabel=Label(window,text="select song",font=("Calibri",10))
    namelabel.place(x=2,y=1)

    listbox=ListBox(window,height=10,width=39,activeStyle="dotbox")
    listbox.place(x=10,y=10)

    
    labelUsers=Label(window,text="activeUsers",font=("Calibri",10))
    labelUsers.place(x=10,y=50)

    listbox=Listbox(window,height=5,width=67,activestyle='dotbox',font=("Calibri",10))
    listbox.place(x=10,y=70)

    scrollbar1=Scrollbar(listbox)
    scrollbar1.place(relheight=1,relx=1)
    scrollbar1.config(command=listbox.yview)

    

    stop=Button(window,text="stop",bd=1,font=("Calibri",10))
    stop.place(x=282,y=160)

    playbutton=Button(window,text="play",bd=1,font=("Calibri",10))
    playbutton.place(x=350,y=160)

    download=Button(window,text="download",bd=1,font=("Calibri",10))
    download.place(x=435,y=160)

    labelchat=Label(window,text="chat window",fon=("Calibri",10))
    labelchat.place(x=10,y=180)

    infolabel=Text(window,text="",fg="blue",font=("Calibri",10))
    infolabel.place(x=10,y=200)

    upload=Button(window,text="upload",bd=1,font=("Calibri",10))
    upload.place(x=10,y=305)

    window.mainloop()





def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    SERVER=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))
    musicWindow()
setup()



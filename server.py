import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog 


IP_ADDRESS='127.0.0.1'
PORT=8080
SERVER=None
clients={}
BUFFER_SIZE=None




    
def acceptConnections():
    global SERVER
    global clients
    while True:
        client,addr=SERVER.accept()
        client_name=client.recv(4096).decode().lower()
        clients[client_name]={
            "client":client,
            "address":addr,
            "connected_with":"",
            "file_name":"",
            "file_size":4096

        }

def setup():
    print("\n\t\t\t\t\tIP MESSENGER")
    global PORT
    global IP_ADDRESS
    global SERVER
    SERVER=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))
    SERVER.listen(100)
    print("\t\t\tserver is waiting for incoming connection...")
    print("\n")
    acceptConnections()
    

setup_thread=Thread(target=setup)
setup_thread.start()



    





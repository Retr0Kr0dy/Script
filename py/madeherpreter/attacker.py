__author__ = 'RetR0'

import threading
import socket

host = '192.168.248.158'
port = int('55555')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect ((host, port))

def reciv():
    message = client.recv(2048)
    message = message.decode()
    print (message)

def main():
    while True:
        a = bytearray(input(f"HACKER@{host}#").encode('utf-8'))
        if len(a) == 0:
            main()
        if a.decode() == "QUIT":
            client.close()
            quit()
        client.send(a)
        reciv()

main()

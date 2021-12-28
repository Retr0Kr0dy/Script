__author__ = 'RetR0'

import threading
import socket

host = input ("Enter the IP of the host server :")
port = int(input ("Enter the listening port of the host server :"))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect ((host, port))


def main():
    while True:
        try:
            message = client.recv(3072)   
            print(message)         
        except:
            print("\nDisconected from the server !")
            client.close()
            break

def send_message():
    while True:
        messa = input("")
        message = messa
        client.send(message)


main_thread = threading.Thread(target=main)
main_thread.start()

send_message_thread = threading.Thread(target=send_message)
send_message_thread.start()

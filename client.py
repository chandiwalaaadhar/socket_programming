import socket
import threading


HEADER=64
PORT=8080
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE="!!!DISCONNECTED!!!"

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    msg_len=len(message)
    send_len=str(msg_len).encode(FORMAT)
    send_len+= b' '*(HEADER-len(send_len))
    client.send(send_len)
    client.send(message)

    print(client.recv(1024).decode(FORMAT))


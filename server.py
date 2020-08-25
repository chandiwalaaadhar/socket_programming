import socket
import threading

HEADER=64
PORT=8080
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE="!!!DISCONNECTED!!!"

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def start():
    server.listen()
    print(f"[LISTENING] The Server {SERVER} is Listening")
    while True:
        conn, addr = server.accept()
        thread=threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Number of active connections are {threading.activeCount()-1}")

def handle_client(conn, addr):
    print(f"NEW CONNECTION is active on {addr}")

    connected=True
    while connected:
        msg_len=conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len=int(msg_len)
            msg=conn.recv(msg_len).decode(FORMAT)
            if msg=='DISCONNECT_MESSAGE':
                connected=False
            print(f"[{addr}] {msg}")
            conn.send("Message is Received".encode(FORMAT))
    conn.close()

print("SERVER IS STARTING......")
start()
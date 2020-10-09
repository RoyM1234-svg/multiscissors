import socket
import threading
import time

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print (f"[NEW CONNECTIONS] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            else:
                conn.send(f"You picked to be {msg}".encode(FORMAT))

            print (f"[{addr}] {msg}")
            
    conn.close()

def start():
    server.listen(2)
    print (f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        new_thread = threading.Thread(target=handle_client, args= (conn,addr))
        new_thread.start()
        print (f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        
print ("[SERVER IS STARTING]")
start()

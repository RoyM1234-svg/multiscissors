import socket

HEADER = 64
PORT = 5050
SERVER = "192.168.0.107"
FORMAT = "utf-8"
ADDR = (SERVER,PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

kind = input("choose kind:")
send(kind)
send(DISCONNECT_MESSAGE)

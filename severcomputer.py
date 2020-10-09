import socket
from _thread import *
import sys
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '192.168.0.107'
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

        
currentId = "0"
kinds_list = ["none","none"]
def threaded_client(conn):
    global currentId
    conn.send(str.encode(currentId))
    currentId = "1"
    kind = ''
    while True:
        try:
            data = conn.recv(2048)
            kind = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                print("Recieved: " + kind)
                arr = kind.split(":")
                id = int(arr[0])
                kinds_list.insert(id, arr[1])

                if id == 0: nid = 1
                if id == 1: nid = 0

                print("player " + arr[0] + " chose" + arr[1])
                # print(json.dumps(kinds_list))

            reply = kinds_list[nid]    
            conn.sendall(str.encode(reply))
        except:
            break

    print("Connection Closed")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))
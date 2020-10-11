import socket
from _thread import *
import sys
from Game import Game

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '192.168.0.107'
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen()
print("Waiting for a connection")

        

IdCount = "0"
def threaded_client(conn,p):
    # global currentId
    # conn.send(str.encode(currentId))
    # currentId = "1"
    # kind = ''
    # while True:
    #     try:
    #         data = conn.recv(2048)
    #         kind = data.decode('utf-8')
    #         if not data:
    #             conn.send(str.encode("Goodbye"))
    #             break
    #         else:
    #             print("Recieved: " + kind)
    #             arr = kind.split(":")
    #             id = int(arr[0])
    #             kinds_list.insert(id, arr[1])

    #             if id == 0: nid = 1
    #             if id == 1: nid = 0

    #             print("player " + arr[0] + " chose" + arr[1])
    #             # print(json.dumps(kinds_list))

    #         reply = kinds_list[nid]    
    #         conn.sendall(str.encode(reply))
    #     except:
    #         break

    # print("Connection Closed")
    # conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    p = 0
    Idcount +=1
    if Idcount == 1:
        game = Game()
        print ("creating the game")
    else:
        game.ready = True
        p = 1
    
    start_new_thread(threaded_client, (conn,p))
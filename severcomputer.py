import socket
from _thread import *
import sys
from Game import Game
import pickle

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

IdCount = 0
# movelist = [None,None]
def threaded_client(conn,p,game):
    conn.send(str.encode(str(p)))
    # reply = ""
    while True: 
        data = conn.recv(2048).decode()
        if data == "get":
            conn.sendall(pickle.dumps(game))
        elif "get" in data:
            data.replace("get","")
            game.play(p,data)
            conn.sendall(pickle.dumps(game))
        elif data:
            game.play(p,data)
            print(f"player{p+1} chose {data}")
            # movelist[p] = data
            conn.sendall(pickle.dumps(game))
        # elif data == "dosconnect":
        #     break
    print ("Connection Closed")
    conn.close()

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
    IdCount += 1
    if IdCount == 1:
        game= Game()
        print ("creating the game")
    else:
        game.ready = True
        p = 1
    
    start_new_thread(threaded_client, (conn,p,game))
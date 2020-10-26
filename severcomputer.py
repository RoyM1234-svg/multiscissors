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

current_round = 1
IdCount = 0
movelist = [None,None]
def threaded_client(conn,p,game):
    conn.send(str.encode(str(p)))
    # reply = ""
    while True: 
        try:
            data = conn.recv(2048).decode()
            if data == "get":
                conn.sendall(pickle.dumps(game))
            elif data == "reset":
                game.resetWent()
                conn.sendall(pickle.dumps(game))
            elif data == "disconnect":
                print(f"player{p+1} disconnected")
                break
            elif data:
                game.play(p,data)
                print(f"player{p+1} chose {data}")
                movelist[p] = data
                conn.sendall(pickle.dumps(game))
        except:
            break
        
        
        #     game.resetWent()
        
    print ("Connection Closed")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    p = 0
    IdCount += 1
    if IdCount % 2 == 1:
        game= Game()
        print ("creating the game")
    else:
        game.ready = True
        p = 1
    print(p)
    start_new_thread(threaded_client, (conn,p,game))
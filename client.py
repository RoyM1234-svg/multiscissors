from network import Network
from Game import Game
import threading


def put_input(n):
    global m
    move = input("choose your move: ")
    m = move

def get_information(n,p):
    while True:
        g = n.send("get")
        if p == 0 and g.p2Went and not g.p1Went: 
            print("\nyour opponent made his move, hurry up!")
            break
        elif p == 1 and g.p1Went and not g.p2Went: 
            print("\nyour opponent made his move, hurry up!")  
            break    
        elif g.bothWent():
            break 


def main():
    run = True
    connected = True
    n = Network()
    p = int(n.getP())
    print ("you are player" ,p+1)
    score =[0,0]
    while connected and 3 not in score:
        t1 = threading.Thread(target = put_input, args=(n,))
        t2 = threading.Thread(target= get_information, args=(n,p,))
        t1.start()
        t2.start()
        t1.join()
        n.send(m)
        t2.join()
        while run: 
            g = n.send("get")
            if g.bothWent():
                if p == 0:
                    print(f"your opponent chose : {g.moves[1]}")
                else:
                    print(f"your opponent chose : {g.moves[0]}")
                if g.winner() == -1:
                    print("its a tie")
                elif g.winner() == p:
                    print("U WON")
                    score[p] += 1
                else:
                    print("U LOST")
                print (f"your current score is {score[p]}")
                # g.resetWent()
                run = False   
    for i in range(len(score)):
        if score[i] == 3:
            print (f"player {i+1} won the game")
    # n.send("disconnect")


                
        




main()
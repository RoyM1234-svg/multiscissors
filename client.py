from network import Network
from Game import Game
import threading


def put_input(n):
    move = input("choose your move: ")
    g = n.send(move)
def main():
    run = True
    connected = True
    n = Network()
    p = int(n.getP())
    print ("you are player" ,p+1)
    while connected:
        t1 = threading.Thread(target = put_input,args=[n])
        t1.join()
        while run:
            g = n.send("get")
            if g.bothWent():
                if p == 0:
                    print(f"your opponent chose : {g.moves[1]}")
                else:
                    print(f"your opponent chose : {g.moves[0]}")
                if g.winner() == -1:
                    print("its a tie")
                else:
                    print(f"{g.winner()+1} has won")
                g.resetWent()
                run = False
            elif p == 0 and g.p2Went:
                print("your opponent made his move, hurry up!")
            elif p == 1 and g.p1Went:
                print("your opponent made his move, hurry up!")        
        connected = False
    n.send("disconnect")


                
        




main()
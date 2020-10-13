from network import Network
from Game import Game

def main():
    run = True
    connected = True
    n = Network()
    p = int(n.getP())
    print ("you are player" ,p+1)
    while connected:
        move = input("choose your move: ")
        g = n.send(move)
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
        connected = False
    n.send("disconnect")


                
        




main()
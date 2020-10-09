from network import Network


def main():
    n = Network()
    id = n.getid()
    p1 = input("choose your kind: ")
    p2 = n.send(id + ":" + p1)

    if p1 == p2:
        print("its a tie")
    elif p1 == 'paper' and p2 == 'scissors':
        print ("player 2 won")
    elif p1 == 'scissors' and p2 == 'rock':
        print ("player 2 won")
    elif p1 == 'rock' and p2 == 'paper':
        print ("player 2 won")
    else:
        print ("player 1 won")

main()
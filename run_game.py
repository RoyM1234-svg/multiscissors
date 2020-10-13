from network import Network
from Game import Game
import numpy as np

class player(object):
    def __init__(self,kind,num):
        self.kind = kind
        self.num = num

# check game rules and calculate results
def game_rules(p1, p2, score_list):
    if p1.kind == p2.kind:
        return 0
    elif p1.kind == 'paper' and p2.kind == 'scissors':
        score_list[1] += 1
        return p2
    elif p1.kind == 'scissors' and p2.kind == 'rock':
        score_list[1] += 1
        return p2
    elif p1.kind == 'rock' and p2.kind == 'paper':
        score_list[1] += 1
        return p2
    else:
        score_list[0] += 1
        return p1

def create_player(num):
    while True:
        kind = input(f"Player {num}, You choose rock, paper or scissors: ")
        if kind not in ['rock', 'paper', 'scissors']:
            print ("Invalid input. Please try again.")
            continue
        return player(kind,num)

# Check user inputs
def start_game(score_list):
    # Player 1: asks input again if entered anything other than rock, paper, scissors
    p1 = create_player(1)
    p2 = create_player(2)

    return game_rules(p1, p2, score_list)

# Execute game and declare result
def main():
    score_list = np.array([0,0])
    while 3 not in score_list:
            ret = start_game(score_list)
            if ret == 0:
                print ("It's a tie")
            else:
                print ("Congratulations!", ret.num, "wins.")
    if score_list[0] == 3:
        print ("Congratulations! player 1 wins completely.") 
    else:
        print ("Congratulations! player 2 wins completely.")
main()
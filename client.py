from network import Network
from Game import Game
import threading
import time
import pygame
import sys
pygame.init()
width = 900
height = 600
size = (width, height)
screen = pygame.display.set_mode(size)
FONTMENU = pygame.font.SysFont(None, 60)
FONT = pygame.font.SysFont(None, 40)
SMALLFONT = pygame.font.SysFont(None, 30)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
ORNAGE = (255, 127, 80)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# class board:
#     def __init__(self):
#         py.gam

#     def drawboard():
#         pygame.draw.rect(screen,BLACK,(455,(i+1) * 100 + 5, 90, 40)) 


# def put_input(n):
#     global m
#     move = input("choose your move: ")
#     m = move

# def get_information(n,p):
#     while True:
#         g = n.send("get")
#         if p == 0 and g.p2Went and not g.p1Went: 
#             print("\nyour opponent made his move, hurry up!")
#             break
#         elif p == 1 and g.p1Went and not g.p2Went: 
#             print("\nyour opponent made his move, hurry up!")  
#             break    
#         elif g.bothWent():
#             break 
def draw_board():
    draw_scissors()
    draw_rock()
    draw_paper()
    draw_menu()
    # sleep(5)

def message_to_screen(msg, color, FONT, posx, posy):
    message = FONT.render(msg, True, color)
    screen.blit(message, [posx, posy])
    pygame.display.update()


def draw_scissors():
    pygame.draw.rect(screen,WHITE,(400,500, 150, 40)) 
    pygame.display.update()
    msg = "scissors"
    message_to_screen(msg, RED,FONT, 420,510)

def draw_rock():
    pygame.draw.rect(screen,WHITE,(200,500, 150, 40)) 
    pygame.display.update()
    msg = "rock"
    message_to_screen(msg, RED,FONT, 235,510)

def draw_paper():
    pygame.draw.rect(screen,WHITE,(600,500, 150, 40)) 
    pygame.display.update()
    msg = "paper"
    message_to_screen(msg, RED,FONT, 625,510)

def draw_menu():
    msg = "first game"
    message_to_screen(msg, WHITE,FONTMENU, 375,20)
    for i in range(2):
        if i == 0:
            message_to_screen("YOU", BLUE, SMALLFONT, 300 * (i+1), 180)
        else:
            message_to_screen("OPPONENT", BLUE, SMALLFONT, 300 * (i+1), 180)
        pygame.draw.rect(screen,WHITE,(300 * (i+1) - 50,200, 150, 150))
        pygame.draw.rect(screen,BLACK,(300 * (i+1) - 45,205, 140, 140))
        pygame.display.update()    

def get_pick():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            posy = event.pos[1]
            if posx > 400 and posx < 550 and posy > 500 and posy< 545:
                message_to_screen(" scissors", RED, FONT, 260, 220)
                pygame.display.update()
                return "scissors"
            elif posx > 200 and posx < 350 and posy > 500 and posy< 545:
                message_to_screen(" rock", RED, FONT, 260, 220)
                pygame.display.update()
                return "rock"
            elif posx > 600 and posx < 750 and posy > 500 and posy< 545:
                message_to_screen(" paper", RED, FONT, 260, 220)
                pygame.display.update()
                return "paper"

def main():
    connected = True
    n = Network()
    p = int(n.getP())
    draw_board()
    print ("you are player" ,p+1)
    score =[0,0]
    count_rounds = 1
    while connected and 3 not in score:
        run = True
        x = get_pick()
        if x:
            n.send(x)
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
                    else:
                        print("U LOST")
                    score[g.winner()] += 1
                    print (f"your current score is {score[p]}")
                    run = False 
                    count_rounds +=1
                    pygame.draw.rect(screen, BLACK, (0, 0, 900, 600))
                    draw_board()
            pygame.time.delay(500)  
            n.send("reset")
    for i in range(len(score)):
        if score[i] == 3:
            print (f"player {i+1} won the game")
    # n.send("disconnect")


                
        




main()
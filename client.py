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
def draw_board(score,p):
    draw_scissors()
    draw_rock()
    draw_paper()
    draw_menu(score,p)
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

def draw_menu(score,p):
    msg = "first game"
    message_to_screen(msg, WHITE,FONTMENU, 375,20)
    msg1 = f"you are player {p+1}"
    message_to_screen(msg1, GREEN,FONT, 100,20)
    print_score(score,p)
    for i in range(2):
        if i == 0:
            message_to_screen("YOU", BLUE, SMALLFONT, 300 * (i+1), 180) 
        else:
            message_to_screen("OPPONENT", BLUE, SMALLFONT, 300 * (i+1)-25, 180)
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

def cleer_screen():
    pygame.draw.rect(screen, BLACK, (0, 0, 900, 600))

def print_oppmove(g,p):
    if p == 0:
        message_to_screen(g.moves[1], RED, FONT, 570, 220)
    else:
        message_to_screen(g.moves[0], RED, FONT, 570, 220)

def print_won(g,p):
    if g.winner() == -1:
        message_to_screen("its a tie", RED,FONT, 375,90)
    elif g.winner() == p:
        message_to_screen("U WON", RED,FONT, 375,90)
    else:
        message_to_screen("U LOST", RED,FONT, 375,90)

def print_score(score,p):
    msg1 = f"score is = {score[0]} "
    msg2 = f"score is = {score[1]} "
    if p == 0:
        message_to_screen(msg1, BLUE, SMALLFONT, 275, 370)
        message_to_screen(msg2, BLUE, SMALLFONT, 575, 370)
    else:
        message_to_screen(msg2, BLUE, SMALLFONT, 275, 370)
        message_to_screen(msg1, BLUE, SMALLFONT, 575, 370)

def opponent_locked(g,p):
    if p == 0 and g.p2Went: 
        message_to_screen("locked in",RED, FONT, 570, 220)
    elif p == 1 and g.p1Went:
        message_to_screen("locked in",RED, FONT, 570, 220)  

def clear_oppenentlocked():
    pygame.draw.rect(screen,BLACK,(555,205, 140, 140))

       
def main():
    connected = True
    n = Network()
    p = int(n.getP())
    score =[0,0]
    draw_board(score,p)
    count_rounds = 1
    while connected and 3 not in score:
        g = n.send("get")
        opponent_locked(g,p)
        run = True
        x = get_pick()
        if x:
            n.send(x)
            while run: 
                g = n.send("get")
                if g.bothWent():
                    clear_oppenentlocked()
                    print_oppmove(g,p)
                    print_won(g,p)
                    if g.winner() != -1:
                        score[g.winner()] += 1
                    run = False 
                    count_rounds +=1       
            pygame.time.delay(4000)
            cleer_screen()
            draw_board(score,p)   
            n.send("reset")
    for i in range(len(score)):
        if score[i] == 3:
            msgwin = f"PLAYER {i+1} WON THE GAME :)"
            message_to_screen(msgwin, RED,FONT, 375,90)
    pygame.time.delay(4000)
    n.send("disconnect")


                
        

main()
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
Rock = pygame.image.load('rock.png')
Paper = pygame.image.load('paper.png')
Scissors = pygame.image.load('scissors.png')


def draw_board(score,p):
    draw_scissors()
    draw_rock()
    draw_paper()
    draw_menu(score,p)


def message_to_screen(msg, color, FONT, posx, posy):
    message = FONT.render(msg, True, color)
    screen.blit(message, [posx, posy])
    pygame.display.update()


def draw_scissors():
    # pygame.draw.rect(screen,WHITE,(400,500, 150, 40)) 
    screen.blit(Scissors,(420,450))
    pygame.display.update()
    # msg = "scissors"
    # message_to_screen(msg, RED,FONT, 420,510)

def draw_rock():
    # pygame.draw.rect(screen,WHITE,(200,500, 150, 40))
    screen.blit(Rock,(235,450)) 
    pygame.display.update()
    # msg = "rock"
    # message_to_screen(msg, RED,FONT, 235,510)

def draw_paper():
    # pygame.draw.rect(screen,WHITE,(600,500, 150, 40)) 
    screen.blit(Paper,(610,450))
    pygame.display.update()
    # msg = "paper"
    # message_to_screen(msg, RED,FONT, 625,510)

def draw_menu(score,p):
    msg = "RPC"
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
            if posx > 420 and posx < 550 and posy > 450 and posy< 580:
                screen.blit(Scissors,(260,210))
                pygame.display.update()
                return "scissors"
            elif posx > 235 and posx < 365 and posy > 450 and posy< 580:
                screen.blit(Rock,(260,210))
                pygame.display.update()
                return "rock"
            elif posx > 610 and posx < 740 and posy > 450 and posy< 580:
                screen.blit(Paper,(260,210))
                pygame.display.update()
                return "paper"

def clear_screen():
    pygame.draw.rect(screen, BLACK, (0, 0, 900, 600))

def print_oppmove(g,p):
    if p == 0:
        if g.moves[1] == "scissors":
            screen.blit(Scissors,(560,210))
        elif g.moves[1] == "rock": 
            screen.blit(Rock,(560,210))
        else:
            screen.blit(Paper,(560,210))
    else:
        if g.moves[0] == "scissors":
            screen.blit(Scissors,(560,210))
        elif g.moves[0] == "rock": 
            screen.blit(Rock,(560,210))
        else:
            screen.blit(Paper,(560,210))

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
                pygame.event.get()
                g = n.send("get")
                print("get")
                if g.bothWent():
                    clear_oppenentlocked()
                    print_oppmove(g,p)
                    print_won(g,p)
                    if g.winner() != -1:
                        score[g.winner()] += 1
                    run = False 
                    count_rounds +=1       
            pygame.time.delay(4000)
            clear_screen()
            draw_board(score,p)   
            n.send("reset")
    for i in range(len(score)):
        if score[i] == 3:
            msgwin = f"PLAYER {i+1} WON THE GAME :)"
            message_to_screen(msgwin, RED,FONT, 375,90)
    pygame.time.delay(4000)
    n.send("disconnect")


                
        

if __name__ == "__main__":
    main()
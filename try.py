
# import threading
import pygame
import sys
from time import sleep
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

# def put_input():
#     global x 
#     move = input("choose your move: ")
#     x = move

# t1 = threading.Thread(target = put_input)
# t1.start()
# t1.join()
# for i in range(10):
#     print (x)

# x= "paperget"
# data = x.replace("get", "")
# print(data+"i")
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
        msg_player = "player" + str(i+1)
        message_to_screen(msg_player, BLUE, SMALLFONT, 300 * (i+1), 180)
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
def main():
    game_over = False
    draw_board()
    while not game_over:
        x = get_pick()
        if x:
            print(x)
            break
        
main()
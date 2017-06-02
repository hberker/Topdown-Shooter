import pygame
from pygame.locals import *

pygame.init()

display_width = 798
display_height = 538

black = (0,0,0)
white = (255,255,255)
red = (222,75,105)
green = (108,255,123)
dark_red = (255,0,0)
dark_green = (39,255,60)
grey = (100,100,100)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Project')

playerimg = pygame.image.load('___')
enemy = pygame.image.load('___')

clock = pygame.time.Clock()
pygame.display.fill(red)

car_width = 100

pause = False

def player(x,y):
	gameDisplay.blit(playerimg,(x,y))

def messageDis(text):
	largeText=pygame.font.SysFont("comicsansms",90)
	textSurf, textRect = text_objects(text,largeText)
	text.Rect.center = ((display_width/2),(display_height/5))
	gameDisplay.blit(textSurf,textRect)
	
	pygame.display.update()
	time.sleep(2)
	
	start()

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
	
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print 

    if x + w > mouse[0] >x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "start":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "continue":
                unpause()
				
def start():
	playing = True
	
	while playing:
	
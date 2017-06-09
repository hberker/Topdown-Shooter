import pygame
from pygame.locals import *
import time
import random

pygame.init()

print("hello")

screenW = 798
screenH = 538

playerW = 50
playerH = 50
black = (0,0,0)
white = (255,255,255)
red = (222,75,105)
green = (108,255,123)
dark_red = (255,0,0)
dark_green = (39,255,60)
grey = (100,100,100)

screen = pygame.display.set_mode((screenW, screenH))

clock = pygame.time.Clock()

pygame.display.set_caption('GameProject')

background_image = pygame.image.load('back_ground.png')
playerUp = pygame.image.load('playerUp.png')
screen.fill(grey)
playerRight = pygame.image.load('playerRight.png')
playerDown = pygame.image.load('playerDown.png')
playerLeft = pygame.image.load('playerLeft.png')

##enemy = pygame.image.load('____')

playerW = 100
playerH = 100

def player(x,y,direction):
    screen.blit(direction,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont("comicsansms",90)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((screenW/2),(screenH/5))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    gameScreen()


def unpause():
    global pause
    pause = False


def paused():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(background_image, [0, 0])
        largeText = pygame.font.SysFont("comicsansms", 90)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((screenW / 2), (screenH / 5))
        screen.blit(TextSurf, TextRect)

        button("Continue", 200, 200, 400, 200, dark_green, green, "continue")
        button("QUIT", 300, 425, 200, 100, dark_red, red, "quit")

        pygame.display.update()
        clock.tick(15)


def death():
    message_display('You Died')
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "Begin":
                game_loop()
            elif action == "End Game":
                pygame.quit()
                quit()
            elif action == "continue":
                unpause()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

        smallText = pygame.font.SysFont("comicsansms", 40)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x + (w / 2)), y + (h / 2))
        screen.blit(textSurf, textRect)


def gameScreen():
    start = True

    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(grey)
        #screen.blit(background_image, [0, 0])

        largeText = pygame.font.SysFont("comicsansms", 90)
        TextSurf, TextRect = text_objects("Game Project", largeText)
        TextRect.center = ((screenW / 2), (screenH / 5))
        screen.blit(TextSurf, TextRect)

        button("PLAY", 200, 200, 400, 200, dark_green, green, "Begin")
        button("QUIT", 300, 425, 200, 100, dark_red, red, "End Game")

        mouse = pygame.mouse.get_pos()

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause
    x = (screenW * 0.45)
    y = (screenH * 0.7)

    x_change = 0
    y_change = 0
    direction = playerUp
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                    direction = playerLeft
                if event.key == pygame.K_RIGHT:
                    x_change = 10
                    direction = playerRight
                if event.key == pygame.K_UP:
                    y_change = -10
                    direction = playerUp
                if event.key == pygame.K_DOWN:
                    y_change = 10
                    direction = playerDown
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or pygame.K_UP or pygame.K_DOWN:
                    x_change = 0
                    y_change = 0


        x += x_change
        y += y_change
        #screen.blit(background_image, [0, 0])
        screen.fill(grey)
        player(x, y,direction)
        pygame.display.update()

        if x > screenW - playerW or x < 0:
            death()
        if y > screenH - playerH or y < 0:
            death()


        clock.tick(70)

gameScreen()
game_loop()

pygame.quit()
quit()


import pygame
import random
import shelve
from os import path

import math

img_dir = path.join(path.dirname(__file__),'img')
pygame.init()

firstGame = True

d = shelve.open('score.txt')
#d['score']= 0
highscore = d['score']



togglerImg = pygame.image.load(path.join(img_dir,('toggle.png')))

ammocart = pygame.image.load(path.join(img_dir,('ammo.png')))

#rifle = pygame.image.load('rifle.png')
rifle = pygame.image.load(path.join(img_dir,"rifle.png"))
shotgun = False
machinegun = False

getGun = 0 #(random.randrange(1,10) - 1)
getMachine = 0#(random.randrange(12,17) - 1)
print(getGun)
loseGun = (random.randrange(1,5) + getGun)
print(loseGun)

numShots = 100
ups = 0

machinegunImg = pygame.image.load(path.join(img_dir,('machinegun1.png')))
playerUp = pygame.image.load(path.join(img_dir,('playerUp.png')))
playerRight = pygame.image.load(path.join(img_dir,('playerRight.png')))
playerDown = pygame.image.load(path.join(img_dir,('playerDown.png')))
playerLeft = pygame.image.load(path.join(img_dir,('playerLeft.png')))
playerUpRight = pygame.image.load(path.join(img_dir,('playerUpRight.png')))
playerDownRight = pygame.image.load(path.join(img_dir,('playerBottomRight.png')))
playerDownLeft = pygame.image.load(path.join(img_dir,('playerBottomLeft.png')))
playerUpLeft = pygame.image.load(path.join(img_dir,('playerTopLeft.png')))

bulletimg = pygame.image.load(path.join(img_dir,('bullet.png')))
background = pygame.image.load(path.join(img_dir,('grass_14.png')))
medpac = pygame.image.load(path.join(img_dir,('med.jpg')))
shotgunImg = pygame.image.load(path.join(img_dir,('shotgun.png')))

rifleimg = pygame.transform.scale(rifle, (70, 20))
x = pygame.transform.scale(shotgunImg, (70, 20))
toggle = pygame.transform.scale(togglerImg, (90, 40))
y = pygame.transform.scale(machinegunImg, (50, 20))

screenW = 640
screenH = 640
FPS = 60
playerPos = playerUp
playerPos1 = playerUp
playerHealth = 100
numenem = 1

keys = {'right':False, 'up':False, 'left':False, 'down':False}
keys2 = {'right': False, 'up': False, 'left': False, 'down': False}

playerW = 30
playerH = 50



black = (0,0,0)
white = (255,255,255)
red = (222,75,105)
bright_green = (70,182,77)
green = (108,255,123)
dark_red = (255,0,0)
dark_green = (39,255,60)
grey = (100,100,100)
blue = (0,0,255)
yellow = (255,255,51)

font_name = pygame.font.match_font('arial')
def imagetoggle(shotgun,machinegun,guntype):
    x = pygame.transform.scale(shotgunImg, (70, 20))
    screen.blit(x, (540, 600))
    y = pygame.transform.scale(machinegunImg, (50, 20))
    screen.blit(y, (460, 600))
    screen.blit(rifleimg,(380, 600))
    if shotgun and GunType['shotGun']:
        screen.blit(toggle,(530,590))
        screen.blit(x, (540, 600))
    elif machinegun and GunType['MachineGun']:
        screen.blit(toggle, (450, 590))
        screen.blit(y, (460, 600))
    else:
        screen.blit(toggle,(370,590))
        screen.blit(rifleimg,(380,600))


def ammobar(numshots):
    if numShots > 75:
        barColor = green
    elif numShots > 50:
        barColor = yellow
    else:
        barColor = red
    pygame.draw.rect(screen,black,(30,70,580,30))
    pygame.draw.rect(screen, barColor,(40,80, numshots * 5.6, 10))

def healthbar(playerHealth):
    if playerHealth > 75:
        barColor = green
    elif playerHealth > 50:
        barColor = yellow
    else:
        barColor = red
    pygame.draw.rect(screen,black,(30,45,580,30))
    pygame.draw.rect(screen, barColor,(40,55,playerHealth * 5.6, 10))

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def startScreen():
    if firstGame == True:
        screen.fill(black)
        draw_text(screen, "Project", 64, screenW / 2, screenH / 5)
        draw_text(screen, "WASD to Move and Space Bar to Shoot", 40, screenW / 2, screenH / 2)
        draw_text(screen, "Press the 'P' Key to Begin", 40, screenW / 2, screenH / 3)
        pygame.display.flip()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_p:
                        waiting = False
    if firstGame == False:
        d = shelve.open('score.txt')
        highscore = d['score']
        if score > highscore:
            newhighscore = score
            d['score'] = newhighscore
            screen.fill(black)
            draw_text(screen, "Game Over", 64, screenW / 2, screenH / 6)
            draw_text(screen, "New Highscore " + str(score), 40, screenW / 2, screenH / 2)
            draw_text(screen, "Press the 'P' Key to Play Again", 40, screenW / 2, screenH / 3)
            pygame.display.flip()
        else:
            screen.fill(black)
            draw_text(screen, "Game Over", 64, screenW / 2, screenH / 6)
            draw_text(screen, "Your Score " + str(score), 40, screenW / 2, screenH / 2)
            draw_text(screen, "Press the 'P' Key to Play Again", 40, screenW / 2, screenH / 3)
            draw_text(screen, "The Current HighScore is " + str(highscore), 40, screenW / 2, screenH * .6)
            pygame.display.flip()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_p:
                        waiting = False



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image = pygame.transform.scale(playerPos,(playerW, playerH))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.radius = playerW * .85 / 2
        self.rect.center = (screenW/2, screenH/2)
        self.speedx = 0
        self.speedy = 0


    def update(self):
        self.speedx = 0
        self.speedy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.speedx = -3
        if key[pygame.K_d]:
            self.speedx = 3
        if key[pygame.K_w]:
            self.speedy = -3
        if key[pygame.K_s]:
            self.speedy = 3
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > screenW:
            self.rect.left = (screenW - 50)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screenH:
            self.rect.bottom = screenH
        if playerPos == playerUp:
            self.image = pygame.transform.scale(playerUp, (playerW, playerH))
        if playerPos == playerDown:
            self.image = pygame.transform.scale(playerDown, (playerW, playerH))
        if playerPos == playerLeft:
            self.image = pygame.transform.scale(playerLeft, (playerH, playerW))
        if playerPos == playerRight:
            self.image = pygame.transform.scale(playerRight, (playerH, playerW))
        if playerPos == playerUpRight:
            self.image = pygame.transform.scale(playerUpRight, (50, 50))
        if playerPos == playerDownRight:
            self.image = pygame.transform.scale(playerDownRight, (50, 50))
        if playerPos == playerDownLeft:
            self.image = pygame.transform.scale(playerDownLeft, (50, 50))
        if playerPos == playerUpLeft:
            self.image = pygame.transform.scale(playerUpLeft, (50, 50))
    def shootUp(self):
            bullet = Bullet(self.rect.centerx, self.rect.centery)
            all_sprites.add(bullet)
            bullets.add(bullet)
    def shootRight(self):
            bullet = BulletR(self.rect.centerx, self.rect.centery)
            all_sprites.add(bullet)
            bullets.add(bullet)
    def shootLeft(self):
        bullet = BulletL(self.rect.centerx, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)
    def shootDown(self):
        bullet = BulletD(self.rect.centerx, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)
    def shootUpRight(self):
        bullet = BulletUR(self.rect.centerx, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)
    def shootDownRight(self):
        bullet = BulletBR(self.rect.centerx, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)
    def shootDownLeft(self):
        bullet = BulletDL(self.rect.centerx, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)
    def shootUpLeft(self):
        bullet = BulletUL(self.rect.centerx, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image = pygame.transform.scale(playerPos,(playerW, playerH))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.radius = playerW * .85 / 2
        self.rect.center = (screenW/2, screenH/2)
        self.speedx = 0
        self.speedy = 0


    def update(self):
        self.speedx = 0
        self.speedy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.speedx = -3
        if key[pygame.K_RIGHT]:
            self.speedx = 3
        if key[pygame.K_UP]:
            self.speedy = -3
        if key[pygame.K_DOWN]:
            self.speedy = 3
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > screenW:
            self.rect.left = (screenW - 50)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screenH:
            self.rect.bottom = screenH
        if playerPos1 == playerUp:
            self.image = pygame.transform.scale(playerUp, (playerW, playerH))
        if playerPos1 == playerDown:
            self.image = pygame.transform.scale(playerDown, (playerW, playerH))
        if playerPos1 == playerLeft:
            self.image = pygame.transform.scale(playerLeft, (playerH, playerW))
        if playerPos1 == playerRight:
            self.image = pygame.transform.scale(playerRight, (playerH, playerW))
        if playerPos1 == playerUpRight:
            self.image = pygame.transform.scale(playerUpRight, (50, 50))
        if playerPos1 == playerDownRight:
            self.image = pygame.transform.scale(playerDownRight, (50, 50))
        if playerPos1 == playerDownLeft:
            self.image = pygame.transform.scale(playerDownLeft, (50, 50))
        if playerPos1 == playerUpLeft:
            self.image = pygame.transform.scale(playerUpLeft, (50, 50))
    def shootUp(self):
            bullet = Bullet(self.rect.topx, self.rect.centery)
            all_sprites.add(bullet)
            bullets.add(bullet)
    def shootRight(self):
            bullet = BulletR(self.rect.rightx, self.rect.centery)
            all_sprites.add(bullet)
            bullets.add(bullet)
    def shootLeft(self):
        bullet = BulletL(self.rect.leftx, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)
    def shootDown(self):
        bullet = BulletD(self.rect.centerx, self.rect.bottomy)
        all_sprites.add(bullet)
        bullets.add(bullet)
    def shootUpRight(self):
        bullet = BulletUR(self.rect.topx, self.rect.righty)
        all_sprites.add(bullet)
        bullets.add(bullet)
    def shootDownRight(self):
        bullet = BulletBR(self.rect.rightx, self.rect.bottomy)
        all_sprites.add(bullet)
        bullets.add(bullet)
    def shootDownLeft(self):
        bullet = BulletDL(self.rect.centerx, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)
    def shootUpLeft(self):
        bullet = BulletUL(self.rect.centerx, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletimg
        self.image = pygame.transform.scale(bulletimg, (15, 15))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
class BulletR(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletimg
        self.image.set_colorkey(white)
        self.image = pygame.transform.scale(bulletimg, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.speedy = 0
        self.speedx = 10
    def update(self):
        self.rect.x += self.speedx
        if self.rect.left > screenW:
            self.kill()
class BulletL(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletimg
        self.image = pygame.transform.scale(bulletimg, (15, 15))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.speedy = 0
        self.speedx = -10
    def update(self):
        self.rect.x += self.speedx
        if self.rect.right < 0:
            self.kill()

class BulletD(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletimg
        self.image.set_colorkey(white)
        self.image = pygame.transform.scale(bulletimg, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.speedy = 10
        self.speedx = 0
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > screenH:
            self.kill()
class BulletUR(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletimg
        self.image.set_colorkey(white)
        self.image = pygame.transform.scale(bulletimg, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.speedy = -10
        self.speedx = 10
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.left > screenW:
            self.kill()

class BulletBR(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletimg
        self.image.set_colorkey(white)
        self.image = pygame.transform.scale(bulletimg, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.speedy = 10
        self.speedx = 10
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > screenH:
            self.kill()
        if self.rect.left > screenW:
            self.kill()
class BulletDL(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletimg
        self.image.set_colorkey(white)
        self.image = pygame.transform.scale(bulletimg, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.speedy = 10
        self.speedx = -10
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > screenH :
            self.kill()
        if self.rect.right < 0:
            self.kill()
class BulletUL(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletimg
        self.image.set_colorkey(white)
        self.image = pygame.transform.scale(bulletimg, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.speedy = -10
        self.speedx = -10
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.right < 0:
            self.kill()
class healthUp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.image = medpac
        self.image = pygame.transform.scale(medpac, (25, 25))
        self.rect = self.image.get_rect()
        self.radius = 20
        #self.rect.x = random.randrange(screenW - self.rect.width)
        #self.rect.y = random.randrange(-100,-40)
        self.rect.x = random.randrange(screenW - self.rect.width)
        self.rect.y = random.randrange(0, (screenH - self.rect.width))
        #self.speedy = random.randrange(1,3)
        #self.speedx = random.randrange(-2,2)
    def update(self):
        #self.rect.x += self.speedx
        #self.rect.y += self.speedy
        if self.rect.top > screenH + 10:
            self.rect.x = random.randrange(screenW - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            #self.speedy = random.randrange(1, 3)
            #self.speedx = random.randrange(-1, 1)
class Ammo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.image = ammocart
        self.image = pygame.transform.scale(ammocart, (25, 25))
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.x = random.randrange(screenW - self.rect.width)
        self.rect.y = random.randrange(0, (screenH - self.rect.width))

        #self.speedy = random.randrange(1,3)
        #self.speedx = random.randrange(-1,1)
    def update(self):
        #self.rect.x += self.speedx
        #self.rect.y += self.speedy
        if self.rect.top > screenH + 10:
            self.rect.x = random.randrange(screenW - self.rect.width)
            self.rect.y = random.randrange(0, (screenH - self.rect.width))
            #self.speedy = random.randrange(1, 3)
            #self.speedx = random.randrange(-1, 1)


all_sprites = pygame.sprite.Group()
ammoUps = pygame.sprite.Group()
powerUps = pygame.sprite.Group()
player = Player()
player2 = Player2()
bullets = pygame.sprite.Group()


all_sprites.add(player)
all_sprites.add(player2)

screen = pygame.display.set_mode((screenW, screenH))
clock = pygame.time.Clock()



pygame.display.set_caption('GameProject')
on = True
game_over = True
score = 0
shootdir = 0
shootdir2 = 0
newshootdir = 0
GameSteper = 0

def createPowerUp(x):
    for i in range(x):
        p = healthUp()
        all_sprites.add(p)
        powerUps.add(p)
def createAmmoCart(x):
    for i in range(x):
        a = Ammo()
        all_sprites.add(a)
        ammoUps.add(a)
while on:
    shooting = True
    if game_over:
        startScreen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        enemys = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        player = Player()
        player2 = Player2()
        all_sprites.add(player)
        all_sprites.add(player2)

        GunType = {'shotGun': False, 'MachineGun': False, 'Rifle': True}
        keys = {'right': False, 'up': False, 'left': False, 'down': False}
        keys2 = {'right': False, 'up': False, 'left': False, 'down': False}

        score = 0
        ups = 0
        machinegun = False
        shotgun = False
        numShots = 100
        GameSteper = 0
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys['up'] = True
            if event.key == pygame.K_a:
                keys['left'] = True
            if event.key == pygame.K_s:
                keys['down'] = True
            if event.key == pygame.K_d:
                keys['right'] = True
            if event.key == pygame.K_UP:
                keys2['up'] = True
            if event.key == pygame.K_LEFT:
                keys2['left'] = True
            if event.key == pygame.K_DOWN:
                keys2['down'] = True
            if event.key == pygame.K_RIGHT:
                keys2['right'] = True
            if event.key == pygame.K_SPACE:
                if shootdir == 1:
                    player.shootUp()
                if shootdir == 2:
                    player.shootRight()
                if shootdir == 3:
                    player.shootLeft()
                if shootdir == 4:
                    player.shootDown()
                if shootdir == 5:
                    player.shootUpRight()
                if shootdir == 8:
                    player.shootDownRight()
                if shootdir == 6:
                    player.shootUpLeft()
                if shootdir == 7:
                    player.shootDownLeft()
            if event.key == pygame.K_RSHIFT:
                if shootdir == 1:
                    player2.shootUp()
                if shootdir == 2:
                    player2.shootRight()
                if shootdir == 3:
                    player2.shootLeft()
                if shootdir == 4:
                    player2.shootDown()
                if shootdir == 5:
                    player2.shootUpRight()
                if shootdir == 8:
                    player2.shootDownRight()
                if shootdir == 6:
                    player2.shootUpLeft()
                if shootdir == 7:
                    player2.shootDownLeft()



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                keys['right'] = False
            if event.key == pygame.K_w:
                keys['up'] = False
            if event.key == pygame.K_s:
                keys['down'] = False
            if event.key == pygame.K_a:
                keys['left'] = False
            if event.key == pygame.K_RIGHT:
                keys2['right'] = False
            if event.key == pygame.K_UP:
                keys2['up'] = False
            if event.key == pygame.K_DOWN:
                keys2['down'] = False
            if event.key == pygame.K_LEFT:
                keys2['left'] = False

        if keys2['right']:
            shootdir = 2
            Player2()
            playerPos1 = playerRight
        if keys2['up']:
            shootdir = 1
            Player2()
            playerPos1 = playerUp
        if keys2['left']:
            shootdir = 3
            Player2()
            playerPos1 = playerLeft
        if keys2['down']:
            shootdir = 4
            Player2()
            playerPos1 = playerDown
        if keys2['right'] and keys['up']:
            shootdir = 5
            Player2()
            playerPos1 = playerUpRight
        if keys2['up'] and keys['left']:
            shootdir = 6
            Player2()
            playerPos1 = playerUpLeft
        if keys2['left'] and keys['down']:
            shootdir = 7
            Player2()
            playerPos1 = playerDownLeft
        if keys['right'] and keys['down']:
            shootdir = 8
            Player()
            playerPos = playerDownRight
        if keys['right']:
            shootdir = 2
            Player()
            playerPos = playerRight
        if keys['up']:
            shootdir = 1
            Player()
            playerPos = playerUp
        if keys['left']:
            shootdir = 3
            Player()
            playerPos = playerLeft
        if keys['down']:
            shootdir = 4
            Player()
            playerPos = playerDown
        if keys['right'] and keys['up']:
            shootdir = 5
            Player()
            playerPos = playerUpRight
        if keys['up'] and keys['left']:
            shootdir = 6
            Player()
            playerPos = playerUpLeft
        if keys['left'] and keys['down']:
            shootdir = 7
            Player()
            playerPos = playerDownLeft
        if keys['right'] and keys['down']:
            shootdir = 8
            Player()
            playerPos = playerDownRight

    background_rect = background.get_rect()
    all_sprites.update()
    player1col = pygame.sprite.spritecollide(player, bullets,True)
    player2col = pygame.sprite.spritecollide(player2,bullets,True)
    ammoCols = pygame.sprite.spritecollide(player, ammoUps, True)
    powerCols = pygame.sprite.spritecollide(player, powerUps, True)
    cols = pygame.sprite.groupcollide(bullets, enemys, True, True)
    colsE = pygame.sprite.spritecollide(player, enemys, True, pygame.sprite.collide_circle)


    if powerCols:
        if playerHealth == 100:
            print("Full health")
        else:
            playerHealth += 10
    if ammoCols:
        if numShots == 100:
            print("cant carry anymore ammo")
        if numShots + 50 > 100:
            numShots = 100
        else:
            numShots += 50
    for i in colsE:
        if playerHealth == 0:

            playerHealth = 100
            game_over = True
            firstGame = False
        else:
            playerHealth -= 10








    screen.fill(white)
    screen.blit(background, background_rect)
    imagetoggle(shotgun,machinegun, GunType)
    healthbar(playerHealth)
    ammobar(numShots)
    all_sprites.draw(screen)
    draw_text(screen, "Kills " + str(score), 30, screenW / 2, 10)
    pygame.display.flip()
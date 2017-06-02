import pygame
import random
import shelve
import math
pygame.init()

firstGame = True
d = shelve.open('score.txt')
d['score']= 0
highscore = d['score']
EnemyUpLeft = pygame.image.load('UpLeft.png')
EnemyUpRight = pygame.image.load('UpRight.png')
EnemyRight = pygame.image.load('Right.png')
EnemyDown = pygame.image.load('Down.png')
EnemyDownLeft = pygame.image.load('DownLeft.png')
EnemyDownRight = pygame.image.load('DownRight.png')
EnemyUp = pygame.image.load('Up1.png')
EnemyLeft = pygame.image.load('Left1.png')

ammocart = pygame.image.load('ammo.png')

shotgun = False

getGun = (random.randrange(1,10) - 1)
print(getGun)
loseGun = (random.randrange(1,5) + getGun)
print(loseGun)

numShots = 100
ups = 0
playerUp = pygame.image.load('playerUp.png')
playerRight = pygame.image.load('playerRight.png')
playerDown = pygame.image.load('playerDown.png')
playerLeft = pygame.image.load('playerLeft.png')
playerUpRight = pygame.image.load('playerUpRight.png')
playerDownRight = pygame.image.load('playerBottomRight.png')
playerDownLeft = pygame.image.load('playerBottomLeft.png')
playerUpLeft = pygame.image.load('playerTopLeft.png')

bulletimg = pygame.image.load('bullet.png')
background = pygame.image.load('grass_14.png')
medpac = pygame.image.load('med.jpg')
shotgunImg = pygame.image.load('shotgun.png')

screenW = 640
screenH = 640
FPS = 60
EnemyPos = EnemyDown
playerPos = playerUp
playerPos1 = playerUp
playerHealth = 100
numenem = 1

playerW = 30
playerH = 50

EnemyW = 30
EnemyH = 50

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
        bullet = BulletR(self.rect.centerx,self.rect.centery)
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

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speedy = random.randrange(1, 3)
        self.speedx = 0
        self.image = pygame.Surface((40,40))
        self.image.set_colorkey(black)
        self.image = pygame.transform.scale(EnemyPos, (40, 40))
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.x = random.randrange(screenW - self.rect.width)
        self.rect.y = 2#random.randrange(-15,-10)
    def update(self):

        dx = 0; dy = 0
        if self.rect.x < player.rect.x:
            dx += 1
        else:
            dx -= 1
        if self.rect.y < player.rect.y:
            dy += 1
        else:
            dy -= 1
        EnemyPos = EnemyDown
        if player.rect.top > (self.rect.top - 25) and player.rect.bottom < (self.rect.bottom + 25):
            if player.rect.right < self.rect.left:
                EnemyPos = EnemyLeft
            else:
                EnemyPos = EnemyRight
        elif player.rect.top > self.rect.bottom:
            if player.rect.right < self.rect.left:
                EnemyPos = EnemyDownLeft
            elif player.rect.left > self.rect.right:
                EnemyPos = EnemyDownRight
            elif player.rect.left > self.rect.left and player.rect.right < self.rect.right:
                EnemyPos = EnemyDown

        elif player.rect.bottom < self.rect.top:
            if player.rect.right < self.rect.left:
                EnemyPos = EnemyUpLeft
            elif player.rect.left > self.rect.right:
                EnemyPos = EnemyUpRight
            else: #player.rect.left > self.rect.left and player.rect.right < self.rect.right:
                EnemyPos = EnemyUp


        self.image = EnemyPos
        if EnemyPos == EnemyUp:
            self.image = pygame.transform.scale(EnemyUp, (40, 40))
        if EnemyPos == EnemyDown:
            self.image = pygame.transform.scale(EnemyDown, (40, 40))
        if EnemyPos == EnemyLeft:
            self.image = pygame.transform.scale(EnemyLeft, (40, 40))
        if EnemyPos == EnemyRight:
            self.image = pygame.transform.scale(EnemyRight, (40, 40))
        if EnemyPos == EnemyUpRight:
            self.image = pygame.transform.scale(EnemyUpRight, (40, 40))
        if EnemyPos == EnemyDownRight:
            self.image = pygame.transform.scale(EnemyDownRight, (40, 40))
        if EnemyPos == EnemyDownLeft:
            self.image = pygame.transform.scale(EnemyDownLeft, (40, 40))
        if EnemyPos == EnemyUpLeft:
            self.image = pygame.transform.scale(EnemyUpLeft, (40, 40))
        if self.rect.top > screenH:
            self.rect.x = random.randrange(screenW - self.rect.width)
            self.rect.y = random.randrange(-50, -40)
            self.speedy = random.randrange(1, 3)

        if self.rect.left > screenW:
            self.rect.x = random.randrange(screenW - self.rect.width)
            self.rect.y = random.randrange(-50, -40)
            self.speedy = random.randrange(1, 3)

        if self.rect.right < 0:
            self.rect.x = random.randrange(screenW - self.rect.width)
            self.rect.y = random.randrange(-50, -40)
            self.speedy = random.randrange(1, 3)

        self.rect.x += (dx )
        self.rect.y += (dy * self.speedy)


class EnemyY(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.speedx = random.randrange(1, 3)
        #self.speedy = random.randrange(, 2)
        self.speedy = 0
        self.image = pygame.Surface((40, 40))
        if self.speedy == 2:
            EnemyPos = EnemyDownRight
        if self.speedy == -2:
            EnemyPos = EnemyUpRight
        else:
            EnemyPos = EnemyRight
        self.image = EnemyPos
        self.image = pygame.transform.scale(EnemyPos, (40, 40))
        self.rect = self.image.get_rect()

        self.radius = 20
        self.rect.y = random.randrange(screenH - self.rect.width)
        self.rect.x = 2 #random.randrange(-15,-10)


    def update(self):
        dx = 0;
        dy = 0
        if self.rect.x < player.rect.x:
            dx += 1
        else:
            dx -= 1
        if self.rect.y < player.rect.y:
            dy += 1
        else:
            dy -= 1

        EnemyPos = EnemyDown
        if player.rect.top > (self.rect.top - 25) and player.rect.bottom < (self.rect.bottom + 25):
            if player.rect.right < self.rect.left:
                EnemyPos = EnemyLeft
            else:
                EnemyPos = EnemyRight
        elif player.rect.top > self.rect.bottom:
            if player.rect.right < self.rect.left:
                EnemyPos = EnemyDownLeft
            elif player.rect.left > self.rect.right:
                EnemyPos = EnemyDownRight
            elif player.rect.left > self.rect.left and player.rect.right < self.rect.right:
                EnemyPos = EnemyDown

        elif player.rect.bottom < self.rect.top:
            if player.rect.right < self.rect.left:
                EnemyPos = EnemyUpLeft
            elif player.rect.left > self.rect.right:
                EnemyPos = EnemyUpRight
            else:  # player.rect.left > self.rect.left and player.rect.right < self.rect.right:
                EnemyPos = EnemyUp

        self.image = EnemyPos
        if EnemyPos == EnemyUp:
            self.image = pygame.transform.scale(EnemyUp, (40, 40))
        if EnemyPos == EnemyDown:
            self.image = pygame.transform.scale(EnemyDown, (40, 40))
        if EnemyPos == EnemyLeft:
            self.image = pygame.transform.scale(EnemyLeft, (40, 40))
        if EnemyPos == EnemyRight:
            self.image = pygame.transform.scale(EnemyRight, (40, 40))
        if EnemyPos == EnemyUpRight:
            self.image = pygame.transform.scale(EnemyUpRight, (40, 40))
        if EnemyPos == EnemyDownRight:
            self.image = pygame.transform.scale(EnemyDownRight, (40, 40))
        if EnemyPos == EnemyDownLeft:
            self.image = pygame.transform.scale(EnemyDownLeft, (40, 40))
        if EnemyPos == EnemyUpLeft:
            self.image = pygame.transform.scale(EnemyUpLeft, (40, 40))

        if self.rect.top > screenH:
            self.rect.x = random.randrange(screenW - self.rect.width)
            self.rect.y = random.randrange(-50, -40)
            self.speedy = random.randrange(1, 3)
        if self.rect.left > screenW:
            self.rect.y = random.randrange(screenH - self.rect.height)
            self.rect.x = random.randrange(-50, -40)
            self.speedx = random.randrange(1, 3)
        if self.rect.bottom < 0:
            self.rect.x = random.randrange(screenW - self.rect.width)
            self.rect.y = random.randrange(-50, -40)
            self.speedy = random.randrange(1, 3)
        self.rect.x += (dx * self.speedx)
        self.rect.y += (dy) # * self.speedy)

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
class Shotgun(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.image = shotgunImg
        self.image = pygame.transform.scale(shotgunImg, (50, 20))
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
shotGuner = pygame.sprite.Group()
ammoUps = pygame.sprite.Group()
powerUps = pygame.sprite.Group()
player = Player()
enemys = pygame.sprite.Group()
bullets = pygame.sprite.Group()
keys = {'right':False, 'up':False, 'left':False, 'down':False}


all_sprites.add(player)

screen = pygame.display.set_mode((screenW, screenH))
clock = pygame.time.Clock()



pygame.display.set_caption('GameProject')
on = True
game_over = True
score = 0
shootdir = 0
newshootdir = 0
GameSteper = 0

def wavescreen(wave):
    wave = str(wave)
    screen.blit(background, background_rect)
    healthbar(playerHealth)
    ammobar(numShots)
    draw_text(screen, "Kills " + str(score), 30, screenW / 2, 10)
    all_sprites.draw(screen)
    draw_text(screen, wave, 100, screenW / 2, screenH / 3)
    pygame.display.flip()
    pygame.time.delay(2000)

def createEnemyY(x):
    for i in range(x):
        eY = EnemyY()
        all_sprites.add(eY)
        enemys.add(eY)


def createEnemy(x):
    for i in range(x):
        e = Enemy()
        all_sprites.add(e)
        enemys.add(e)
def createShotGun(x):
    e = Shotgun()
    all_sprites.add(e)
    shotGuner.add(e)





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


def create(wave_num, enemys, powerUps, ammoUps):
    wavescreen("Wave: " + str(wave_num))
    createEnemyY(enemys)
    createEnemy(enemys)
    createPowerUp(powerUps)
    createAmmoCart(ammoUps)
while on:

    if game_over:
        startScreen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        enemys = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        player = Player()
        player = Player()
        all_sprites.add(player)
        keys = {'right': False, 'up': False, 'left': False, 'down': False}
        score = 0
        ups = 0
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
            if event.key == pygame.K_SPACE:
                if numShots > 0:
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
                    numShots -= 1
                else:
                    print("out of bullets")
            if event.key == pygame.K_m:
                if shotgun == True:
                    if numShots > 0:
                        if shootdir == 1:
                            player.shootUp()
                            player.shootUpLeft()
                            player.shootUpRight()
                        if shootdir == 2:
                            player.shootRight()
                            player.shootUpRight()
                            player.shootDownRight()
                        if shootdir == 3:
                            player.shootLeft()
                            player.shootUpLeft()
                            player.shootDownLeft()
                        if shootdir == 4:
                            player.shootDown()
                            player.shootDownRight()
                            player.shootDownLeft()
                        if shootdir == 5:
                            player.shootUpRight()
                            player.shootUp()
                            player.shootRight()
                        if shootdir == 8:
                            player.shootDownRight()
                            player.shootRight()
                            player.shootDown()
                        if shootdir == 6:
                            player.shootUpLeft()
                            player.shootUp()
                            player.shootLeft()
                        if shootdir == 7:
                            player.shootDownLeft()
                            player.shootLeft()
                            player.shootDown()
                        numShots -= 5


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                keys['right'] = False
            if event.key == pygame.K_w:
                keys['up'] = False
            if event.key == pygame.K_s:
                keys['down'] = False
            if event.key == pygame.K_a:
                keys['left'] = False

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
    getShotGun = pygame.sprite.spritecollide(player, shotGuner, True)
    ammoCols = pygame.sprite.spritecollide(player, ammoUps, True)
    powerCols = pygame.sprite.spritecollide(player, powerUps, True)
    cols = pygame.sprite.groupcollide(bullets, enemys, True, True)
    colsE = pygame.sprite.spritecollide(player, enemys, True, pygame.sprite.collide_circle)

    if getShotGun:
        shotgun = True
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
    for x in cols:
        score += 1

    if len(enemys) == 0:
        if GameSteper > 6:
            ups = random.randrange(1,3)
        create(GameSteper + 1,GameSteper + 2,ups,ups)
        if GameSteper == getGun:
            createShotGun(1)
        if GameSteper == loseGun:
            shotgun = False

        GameSteper += 1








    screen.fill(white)
    screen.blit(background, background_rect)
    healthbar(playerHealth)
    ammobar(numShots)
    all_sprites.draw(screen)
    draw_text(screen, "Kills " + str(score), 30, screenW / 2, 10)
    pygame.display.flip()
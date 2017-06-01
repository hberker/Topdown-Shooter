import pygame
import random

pygame.init()

playerUp = pygame.image.load('playerUp.png')
playerRight = pygame.image.load('playerRight.png')
playerDown = pygame.image.load('playerDown.png')
playerLeft = pygame.image.load('playerLeft.png')
playerUpRight = pygame.image.load('playerUpRight.png')
bulletimg = pygame.image.load('bullet.png')
background = pygame.image.load('grass_14.png')
screenW = 640
screenH = 640
FPS = 60
playerPos = playerUp
playerPos1 = playerUp
numenem = 1
playerW = 30
playerH = 50
black = (0,0,0)
white = (255,255,255)
red = (222,75,105)
green = (108,255,123)
dark_red = (255,0,0)
dark_green = (39,255,60)
grey = (100,100,100)

font_name = pygame.font.match_font('arial')

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)



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
            print("working")
            self.image = pygame.transform.scale(playerUp, (playerW, playerH))
        if playerPos == playerDown:
            self.image = pygame.transform.scale(playerDown, (playerW, playerH))
        if playerPos == playerLeft:
            self.image = pygame.transform.scale(playerLeft, (playerH, playerW))
        if playerPos == playerRight:
            self.image = pygame.transform.scale(playerRight, (playerH, playerW))
        if playerPos == playerUpRight:
            self.image = pygame.transform.scale(playerUpRight, (50, 50))
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

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.radius = 20
        #self.radius = int(self.radius * 85 / 2)
        self.rect.x = random.randrange(screenW - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(1,3)
        self.speedx = random.randrange(-3,3)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.rect.y += self.speedy
        if self.rect.top > screenH + 10:
            self.rect.x = random.randrange(screenW - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 3)
class EnemyY(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill(black)

        self.rect = self.image.get_rect()
        self.radius = 35
        self.rect.y = random.randrange(screenH - self.rect.width)
        self.rect.x = random.randrange(-50,-20)
        self.speedx = random.randrange(1,3)
        self.speedy = random.randrange(-2,2)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > screenW + 10:
            self.rect.y = random.randrange(screenH - self.rect.height)
            self.rect.x = random.randrange(-100, -40)
            self.speedx = random.randrange(1, 4)
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

background
all_sprites = pygame.sprite.Group()
player = Player()
enemys = pygame.sprite.Group()
bullets = pygame.sprite.Group()



all_sprites.add(player)

screen = pygame.display.set_mode((screenW, screenH))
clock = pygame.time.Clock()

for i in range(numenem):
    e = Enemy()
    all_sprites.add(e)
    enemys.add(e)
for i in range(numenem):
    eY = EnemyY()
    all_sprites.add(eY)
    enemys.add(eY)


pygame.display.set_caption('GameProject')
on = True
score = 0
shootdir = 0
while on:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                shootdir = 1
                Player()
                playerPos = playerUp
            if event.key == pygame.K_d:
                shootdir = 2
                Player()
                playerPos = playerRight
            if event.key == pygame.K_a:
                shootdir = 3
                Player()
                playerPos= playerLeft
            if event.key == pygame.K_s:
                shootdir = 4
                Player()
                playerPos = playerDown


            if event.key == pygame.K_p:
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









    background_rect = background.get_rect()
    all_sprites.update()
    cols = pygame.sprite.groupcollide(bullets,enemys, True, True)
    colsE = pygame.sprite.spritecollide(player, enemys, False, pygame.sprite.collide_circle)

    for col in cols:
        score += 10
        e = Enemy()
        all_sprites.add(e)
        enemys.add(e)

    if colsE:
        print(score)
        on = False

    screen.fill(white)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, "Score " + str(score), 30, screenW / 2, 10)
    pygame.display.flip()

pygame.quit()
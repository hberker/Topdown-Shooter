import pygame
import random
import shelve

pygame.init()

firstGame = True
d = shelve.open('score.txt')
d['score'] = 0
highscore = d['score']
print(highscore)

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

screenW = 640
screenH = 640
FPS = 60
playerPos = playerUp
playerPos1 = playerUp
playerHealth = 100
numenem = 1

playerW = 30
playerH = 50

black = (0, 0, 0)
white = (255, 255, 255)
red = (222, 75, 105)
bright_green = (70, 182, 77)
green = (108, 255, 123)
dark_red = (255, 0, 0)
dark_green = (39, 255, 60)
grey = (100, 100, 100)
blue = (0, 0, 255)
yellow = (255, 255, 51)

font_name = pygame.font.match_font('arial')


def healthbar(playerHealth):
    if playerHealth > 75:
        barColor = green
    elif playerHealth > 50:
        barColor = yellow
    else:
        barColor = red
    pygame.draw.rect(screen, black, (30, 30, 120, 50))
    pygame.draw.rect(screen, barColor, (40, 40, playerHealth, 30))


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
            # draw_text(screen, "The Current HighScore is " + str(highscore), 40, screenW / 2, screenH * .6)
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
        self.image = pygame.Surface((50, 50))
        self.image = pygame.transform.scale(playerPos, (playerW, playerH))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.radius = playerW * .85 / 2
        self.rect.center = (screenW / 2, screenH / 2)
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


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.radius = 20
        # self.radius = int(self.radius * 85 / 2)
        self.rect.x = random.randrange(screenW - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 3)
        self.speedx = random.randrange(-3, 3)

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
        self.image = pygame.Surface((40, 40))
        self.image.fill(black)

        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.y = random.randrange(screenH - self.rect.width)
        self.rect.x = random.randrange(-50, -20)
        self.speedx = random.randrange(1, 3)
        self.speedy = random.randrange(-2, 2)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > screenW + 10:
            self.rect.y = random.randrange(screenH - self.rect.height)
            self.rect.x = random.randrange(-100, -40)
            self.speedx = random.randrange(1, 4)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
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
    def __init__(self, x, y):
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
    def __init__(self, x, y):
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
    def __init__(self, x, y):
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
    def __init__(self, x, y):
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
    def __init__(self, x, y):
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
    def __init__(self, x, y):
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
        if self.rect.top > screenH:
            self.kill()
        if self.rect.right < 0:
            self.kill()


class BulletUL(pygame.sprite.Sprite):
    def __init__(self, x, y):
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
        self.image = pygame.Surface((40, 40))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.radius = 20
        # self.radius = int(self.radius * 85 / 2)
        self.rect.x = random.randrange(screenW - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 3)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > screenH + 10:
            self.rect.x = random.randrange(screenW - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 3)


all_sprites = pygame.sprite.Group()
powerUps = pygame.sprite.Group()
player = Player()
enemys = pygame.sprite.Group()
bullets = pygame.sprite.Group()
keys = {'right': False, 'up': False, 'left': False, 'down': False}

all_sprites.add(player)

screen = pygame.display.set_mode((screenW, screenH))
clock = pygame.time.Clock()

pygame.display.set_caption('GameProject')
on = True
game_over = True
score = 0
shootdir = 0
newshootdir = 0
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
        for i in range(numenem):
            e = Enemy()
            all_sprites.add(e)
            enemys.add(e)

        for i in range(numenem):
            e = EnemyY()
            all_sprites.add(e)
            enemys.add(e)

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

    powerCols = pygame.sprite.spritecollide(player, powerUps, True)
    cols = pygame.sprite.groupcollide(bullets, enemys, True, True)
    colsE = pygame.sprite.spritecollide(player, enemys, True, pygame.sprite.collide_circle)

    if score == 10:
        p = healthUp()
        all_sprites.add(p)
        powerUps.add(p)
        score += 10
    if score == 100:
        for i in range(2):
            eY = EnemyY()
            all_sprites.add(eY)
            enemys.add(eY)
            score += 10
    if score == 200:
        for i in range(1):
            e = Enemy()
            all_sprites.add(e)
            enemys.add(e)
            score += 10
    if score == 400:
        for i in range(6):
            eY = EnemyY()
            all_sprites.add(eY)
            enemys.add(eY)
        for i in range(1):
            p = healthUp()
            all_sprites.add(p)
            powerUps.add(p)
        score += 10
    if score == 1000:
        for i in range(8):
            e = Enemy()
            all_sprites.add(e)
            enemys.add(e)
            score += 10

    if powerCols:
        if playerHealth == 100:
            print("full health")
        else:
            playerHealth += 10

    for col in cols:
        score += 10
        e = Enemy()
        all_sprites.add(e)
        enemys.add(e)

    for cols in colsE:
        e = Enemy()
        all_sprites.add(e)
        enemys.add(e)
        e = EnemyY()
        all_sprites.add(e)
        enemys.add(e)

        if playerHealth == 0:
            if score < 100:
                print(score)
            if 100 < score < 200:
                print(score - 10)
            if 200 < score < 220:
                print(score - 20)
            if 210 < score < 220:
                print(score - 30)
            if score > 209:
                print(score - 40)
            playerHealth = 100
            game_over = True
            firstGame = False
        else:
            playerHealth -= 10

    screen.fill(white)
    screen.blit(background, background_rect)
    healthbar(playerHealth)
    all_sprites.draw(screen)
    draw_text(screen, "Score " + str(score), 30, screenW / 2, 10)
    pygame.display.flip()
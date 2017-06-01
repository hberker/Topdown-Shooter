GameSteper = 0
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
def createPowerUp(x)
    for i in range(x):
        p = healthUp()
        all_sprites.add(p)
        powerUps.add(p)

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
        gamesteper = 0
        createEnemy(2)
        createEnemyY(2)


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
        if keys['right']and keys['up']:
            shootdir = 5
            Player()
            playerPos = playerUpRight
        if keys['up'] and keys['left']:
            shootdir = 6
            Player()
            playerPos = playerUpLeft
        if keys['left']and keys['down']:
            shootdir = 7
            Player()
            playerPos = playerDownLeft
        if keys['right']and keys['down']:
            shootdir = 8
            Player()
            playerPos = playerDownRight

    background_rect = background.get_rect()
    all_sprites.update()

    powerCols = pygame.sprite.spritecollide(player, powerUps, True)
    cols = pygame.sprite.groupcollide(bullets,enemys, True, True)
    colsE = pygame.sprite.spritecollide(player, enemys, True, pygame.sprite.collide_circle)

    if GameSteper == 0:
        createEnemy(1)
        createEnemyY(1)
        GameSteper += 1

    if powerCols:
        if playerHealth == 100:
            print("full health")
        else:
            playerHealth += 10
    for col in cols:
        score += 10
        GameSteper += 1
        if playerHealth == 0:
            print("Score")
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
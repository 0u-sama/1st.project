import pygame
import random
import math
from pygame import mixer

# initialize the pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Background
background = pygame.image.load("background.png")

# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)
explosion_sound = mixer.Sound("explosion.wav")

bullet_sound = mixer.Sound("laser.wav")

# Player
player_img = pygame.image.load("spaceship.png")
playerX = 389
playerY = 520
player_change_x = 0
player_change_y = 0

# Enemy
enemy_img = []
enemyX = []
enemyY = []
enemy_change_x = []
enemy_change_y = []
enemy_num = 6
for i in range(enemy_num):
    enemy_img.append(pygame.image.load("ufo.png"))
    enemyX.append(random.randint(10, 730))
    enemyY.append(random.randint(20, 100))
    enemy_change_x.append(0.2)
    enemy_change_y.append(40)

# Bullet
bullet_img = pygame.image.load("bullet.png")
bulletX = playerX
bulletY = playerY
bulletX_change = 0
bulletY_change = 0.99
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
txt_x = 10
txt_y = 10

# Game over text
go_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    score = font.render("score: " + str(score_value), True, (0, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 10, y - 15))


def isCollision(X1, Y1, X2, Y2):
    distance = math.sqrt((math.pow(X1-X2, 2)) + (math.pow(Y1 - Y2, 2)))
    if distance <= 27:

        return True
    else:
        return False


def game_over_text():
    explosion_sound.play()
    over = font.render("GAME OVER", True, (255, 15, 20))
    screen.blit(over, (300, 300))


running = True
while running:
    # Blue Green White
    screen.fill((20, 50, 100))

    # Putting the background
    screen.blit(background, (0, 0))

    # Buttons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change_x = -0.3
            elif event.key == pygame.K_RIGHT:
                player_change_x = +0.3
            if event.key == pygame.K_UP:
                player_change_y = -0.3
            elif event.key == pygame.K_DOWN:
                player_change_y = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound.play()
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                player_change_x = 0
            if event.key == pygame.K_UP or pygame.K_DOWN:
                player_change_y = 0
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound.play()
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)

    playerX += player_change_x
    playerY += player_change_y
    # stopping the movement at the edges
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if playerY >= 530:
        playerY = 530
    elif playerY <= 400:
        playerY = 400

    # Enemy limits and mvt
    for i in range(enemy_num):
        # Game Over
        if enemyY[i] >= playerY and enemyX[i] >= playerX:
            for j in range(enemy_num):
                enemyY[j] = 2000
            game_over_text()
            break
        elif enemyY[i] >= 600:
            # Game Over
            if enemyY[i] == playerY and enemyX[i] == playerX:
                for j in range(enemy_num):
                    enemyY[j] = 2000
                game_over_text()
                break

        enemyX[i] += enemy_change_x[i]

        if enemyX[i] <= 0:
            enemy_change_x[i] = 0.15
            enemyY[i] += enemy_change_y[i]
        elif enemyX[i] >= 736:
            enemy_change_x[i] = -0.15
            enemyY[i] += enemy_change_y[i]
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound.play()
            bulletY = playerY
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(10, 730)
            enemyY[i] = random.randint(20, 100)
        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement

    if bulletY <= 0:
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    show_score(txt_x, txt_y)

    player(playerX, playerY)
    pygame.display.update()

import pygame
import random
from random import randint

pygame.init()

WIDTH, HEIGHT = 1000, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
running = True

White = (255, 255, 255)
Blue = (0, 0, 255)
Black = (0, 0, 0)

# Ball
radius = 7
ball_x = WIDTH / 2 - radius
ball_y = HEIGHT / 2 - radius
ball_speed = 0.5
ball_speed_X = ball_speed
ball_speed_y = ball_speed

direction = [0, 1]
angle = [0, 1, 2]

# Paddles
paddle_width, paddle_height = 12, 120

left_paddle_x = 50
left_paddle_y = right_paddle_y = HEIGHT / 2 - paddle_height / 2

right_paddle_x = 940

player_B_change = 0
player_A_change = 0

# Gadgets
left_gadget = right_gadget = 0
left_gadget_remaining = right_gadget_remaining = 5


def ball_movement(X, Y):
    global ball_speed_X, ball_speed_y, ball_x, ball_y, ball_speed
    direct = random.choice(direction)
    ang = random.choice(angle)
    if X >= 995:
        ball_x = WIDTH / 2 - radius
        ball_y = randint(100, 400)

        if direct == 0:
            if ang == 0:
                ball_speed_X, ball_speed_y = 0.5, -0.7
            if ang == 1:
                ball_speed_X, ball_speed_y = 0.5, -0.5
            if ang == 2:
                ball_speed_X, ball_speed_y = 0.8, -0.4
        if direct == 1:
            if ang == 0:
                ball_speed_X, ball_speed_y = 0.4, -0.7
            if ang == 1:
                ball_speed_X, ball_speed_y = 0.5, -0.5
            if ang == 2:
                ball_speed_X, ball_speed_y = 0.6, -0.4

    elif X <= 0 + radius:
        ball_x = WIDTH / 2 - radius
        ball_y = randint(100, 400)
        ball_speed_X = ball_speed
        if direct == 0:
            if ang == 0:
                ball_speed_X, ball_speed_y = 0.4, -0.8
            if ang == 1:
                ball_speed_X, ball_speed_y = 0.5, -0.5
            if ang == 2:
                ball_speed_X, ball_speed_y = 0.8, -0.4
        if direct == 1:
            if ang == 0:
                ball_speed_X, ball_speed_y = 0.4, -0.8
            if ang == 1:
                ball_speed_X, ball_speed_y = 0.5, -0.5
            if ang == 2:
                ball_speed_X, ball_speed_y = 0.8, -0.4
        ball_speed_X *= -1

    if Y >= 595:
        ball_speed_y *= -1
    elif Y <= 0 + radius:
        ball_speed_y *= -1
    ball_x += ball_speed_X
    ball_y += ball_speed_y

    # Collision with paddles
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_speed_X *= -1
    if right_paddle_x <= ball_x:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x
            ball_speed_X *= -1

    return ball_x, ball_y, ball_speed_X


def gadgets(left, right):
    global ball_x, ball_speed_X, left_gadget, right_gadget, right_paddle_y, left_paddle_y
    if left_gadget == 1:
        if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
            if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                ball_x = left_paddle_x + paddle_width
                ball_speed_X *= -2.5
                left_gadget = 0
                left -= 1
    if right_gadget == 1:
        if right_paddle_x <= ball_x:
            if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                ball_x = right_paddle_x
                ball_speed_X *= -2.5
                right_gadget = 0
                right -= 1
    if right_gadget == 2:
        right_paddle_y = ball_y - 50
        right_gadget = 0

    if left_gadget == 2:
        left_paddle_y = ball_y - 50
        left_gadget = 0

    return ball_x, ball_speed_X, left_gadget, left, right_gadget, right, right_paddle_y, left_paddle_y


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_B_change = -1
            if event.key == pygame.K_DOWN:
                player_B_change = 1
            if event.key == pygame.K_KP1 and right_gadget_remaining > 0:
                right_gadget = 1
                right_gadget_remaining -= 1
            if event.key == pygame.K_KP2 and right_gadget_remaining > 0:
                right_gadget = 2
                right_gadget_remaining -= 1

            if event.key == pygame.K_z:
                player_A_change = -1
            if event.key == pygame.K_s:
                player_A_change = 1
            if event.key == pygame.K_j and left_gadget_remaining > 0:
                left_gadget = 1
                left_gadget_remaining -= 1
            if event.key == pygame.K_k and left_gadget_remaining > 0:
                left_gadget = 2
                left_gadget_remaining -= 1

        if event.type == pygame.KEYUP:
            player_B_change = 0
            player_A_change = 0

    window.fill(Black)

    # Paddles limits
    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0

    left_paddle_y += player_A_change
    right_paddle_y += player_B_change

    ball_movement(ball_x, ball_y)
    gadgets(left_gadget_remaining, right_gadget_remaining)

    # Objects
    pygame.draw.circle(window, White, (ball_x, ball_y), radius)
    pygame.draw.rect(window, Blue, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(window, Blue, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    if left_gadget == 1:
        pygame.draw.circle(window, White, (left_paddle_x + 6, left_paddle_y + 6), 4)
    if right_gadget == 1:
        pygame.draw.circle(window, White, (right_paddle_x + 6, right_paddle_y + 6), 4)

    pygame.display.update()

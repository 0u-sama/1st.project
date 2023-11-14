import random

import pygame
from sys import exit
from random import randint, choice


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Player
        player_walk_1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load("graphics/Player/jump.png").convert_alpha()
        player_surface = player_walk[player_index]

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 293))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound("audio/jump.mp3")
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 293:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 293:
            self.rect.bottom = 293

    def animation_state(self):
        if self.rect.bottom < 293:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):

        super().__init__()

        if type == "fly":
            fly_frame1 = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
            fly_frame2 = pygame.image.load("graphics/Fly/Fly2.png").convert_alpha()
            self.frame = [fly_frame1, fly_frame2]
            y_pos = randint(50, 120)
        else:
            snail_frame1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
            snail_frame2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
            self.frame = [snail_frame1, snail_frame2]
            y_pos = 293

        self.animation_index = 0
        self.image = self.frame[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(random.randint(900, 1100), y_pos))

    def animation_state(self):
        if type == "fly":
            self.animation_index += 1
        else:
            self.animation_index += 0.2
        if self.animation_index >= len(self.frame):
            self.animation_index = 0
        self.image = self.frame[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x < -100:
            self.kill()


def display_score():
    time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = text_font.render(f"Score: {time}", False, (64, 64, 64))
    score_rec = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rec)
    return time


def enemy_movement(enemy_list):
    if enemy_list:
        for enemy_rect in enemy_list:
            enemy_rect.x -= 5

            if enemy_rect.bottom == 293:
                screen.blit(snail_surface, enemy_rect)
            else:
                screen.blit(fly_surface, enemy_rect)

        enemy_list = [enemy for enemy in enemy_list if enemy.x > -100]
        return enemy_list
    else:
        return []


def collisions(play, enemy):
    if enemy:
        for enemy_rect in enemy:
            if play.colliderect(enemy_rect):
                return False
    return True


def collision_sprite():
    # (sprite, group, bool)
    """player is group single that contains the sprite"""
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True



def player_animation():
    global player_index, player_surface
    # walk or jump
    if player_rect.bottom < 293:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index > len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]


pygame.init()

width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Akram runner")
clock = pygame.time.Clock()

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

text_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# Enemy
snail_frame_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_frame_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_index = 0
snail_surface = snail_frames[snail_index]
# snail_rect = snail_surface.get_rect(midbottom=(700, 293))
fly_frame_1 = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
fly_frame_2 = pygame.image.load("graphics/Fly/Fly2.png").convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_index = 0
fly_surface = fly_frames[fly_index]

enemy_rect_list = []

# Player
player_walk_1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load("graphics/Player/jump.png").convert_alpha()
player_surface = player_walk[player_index]

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

# Gravity
player_gravity = 0

# pygame.Rect(left, top, width, height)
player_rect = player_surface.get_rect(midbottom=(80, 293))

x_change = 4
game_activity = False

start_time = 0

# Intro /// transform.scale(img, (width, height))
player_stand = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rec = player_stand.get_rect(center=(400, 200))
# text, anti antialiasing, color
title_surface = text_font.render("Akram Runner", False, (155, 64, 64))
title_rec = title_surface.get_rect(midtop=(400, 50))
instruction_surface = text_font.render("Press Space to start", False, (111, 196, 169))
instruction_rec = instruction_surface.get_rect(center=(400, 350))
score = 0
score_message = text_font.render(f"Score:{score}", False, (111, 196, 169))
score_message_rect = score_message.get_rect(center=(400, 330))
bg_music = pygame.mixer.Sound("audio/music.wav")

bg_music.play(loops=-1)

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1030)
snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 280)
fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if not game_activity:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_activity = True
                # snail_rect.right = 800
                start_time = int(pygame.time.get_ticks() / 1000)
                x_change = 4
        if game_activity:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(["fly", "snail", "snail", "snail"])))
                """if randint(0, 2):
                    enemy_rect_list.append(snail_surface.get_rect(midbottom=(randint(900, 1100), 293)))
                else:
                    enemy_rect_list.append(fly_surface.get_rect(midbottom=(randint(900, 1100), 80)))"""

            if event.type == snail_animation_timer:
                if snail_index == 0:
                    snail_index = 1
                else:
                    snail_index = 0
                snail_surface = snail_frames[snail_index]
            if event.type == fly_animation_timer:
                if fly_index == 0:
                    fly_index = 1
                else:
                    fly_index = 0
                fly_surface = fly_frames[fly_index]

        if game_activity:
            if event.type == pygame.KEYDOWN and player_rect.y == 209:
                if event.key == pygame.K_SPACE:
                    player_gravity = -18

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.y == 209:
                    if player_rect.collidepoint(event.pos):
                        player_gravity = -18

    """mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed() == (True, False, False):
            player_gravity = -20"""

    if game_activity:
        player_animation()

        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 290))
        # pygame.draw.rect(screen, '#c0e8ec', title_rec, 0, 15)
        # screen.blit(title_surface, title_rec)
        score = display_score()

        # Enemy movement
        enemy_rect_list = enemy_movement(enemy_rect_list)
        # snail_rect.x -= x_change
        # if snail_rect.right <= -100:
        #    snail_rect.left = 800
        #    x_change += 0.5

        # screen.blit(snail_surface, snail_rect)

        # Player
        """player_gravity += 0.85
        player_rect.y += player_gravity"""
        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()
        """if player_rect.y >= 209:
            player_rect.y = 209
            player_gravity = 0"""

        # screen.blit(player_surface, player_rect)
        # collisions
        # if snail_rect.colliderect(player_rect):
        game_activity = collision_sprite()
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rec)
        screen.blit(title_surface, title_rec)
        score_message = text_font.render(f"Score:{score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 330))
        if score == 0:
            screen.blit(instruction_surface, instruction_rec)
        else:
            screen.blit(score_message, score_message_rect)
            # enemy_rect_list = [] or
            enemy_rect_list.clear()
            player_rect.midbottom = (80, 293)
            player_gravity = 0

    pygame.display.update()

    clock.tick(60)

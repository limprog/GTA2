from game import *
from constants import *
import pygame
from MapGenerator.WebGenerator import *
import time

'''
Класс, описывающий сущность игрока
'''


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0
        self.again = 0
        self.map_x = 3
        self.map_y = 3

    def translateMovement(self, keystate):
        key_dict = {'left': keystate[pygame.K_a] or keystate[pygame.K_LEFT],
                    'up': keystate[pygame.K_w] or keystate[pygame.K_UP],
                    "right": keystate[pygame.K_d] or keystate[pygame.K_RIGHT],
                    'down': keystate[pygame.K_s] or keystate[pygame.K_DOWN], "shift": keystate[pygame.K_LSHIFT]}
        return key_dict

    def update(self):
        self.again = 0
        keystate = self.translateMovement(pygame.key.get_pressed())
        abs_speed = 8
        abs_speed_shift = 14
        if keystate['left']:
            self.speedx -= 0.1
            if self.speedx <= -abs_speed:
                self.speedx = -abs_speed

        if keystate['right']:
            self.speedx += 0.1
            if self.speedx >= abs_speed:
                self.speedx = abs_speed

        if keystate['down']:
            self.speedy += 0.1
            if self.speedy >= 8:
                self.speedy = 8

        if keystate['up']:
            self.speedy -= 0.1
            if self.speedy <= -8:
                self.speedy = -8
        if keystate['left'] and keystate["shift"]:
            self.speedx -= 0.3
            if self.speedx <= -abs_speed_shift:
                self.speedx = -abs_speed_shift

        if keystate['right'] and keystate["shift"]:
            self.speedx += 0.3
            if self.speedx >= abs_speed_shift:
                self.speedx = abs_speed_shift

        if keystate['down'] and keystate["shift"]:
            self.speedy += 0.3
            if self.speedy >= abs_speed_shift:
                self.speedy = abs_speed_shift

        if keystate['up'] and keystate["shift"]:
            self.speedy -= 0.3
            if self.speedy <= -abs_speed_shift:
                self.speedy = -abs_speed_shift

        if all(v == 0 for v in keystate.values()):
            if self.speedx <= -0.2:
                self.speedx += 0.2
            elif self.speedx >= 0.2:
                self.speedx -= 0.2
            else:
                self.speedx = 0
            if self.speedy <= -0.2:
                self.speedy += 0.2
            elif self.speedy >= 0.2:
                self.speedy -= 0.2
            else:
                self.speedy = 0

        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.x < 0:
            if self.map_x > 1:
                self.rect.x = WIDTH - 50
                self.again = 1
                self.map_x -= 1
            else:
                self.rect.x = 0

        if self.rect.right > WIDTH:
            if self.map_x < 5:
                self.rect.x = 0
                self.again = 1
                self.map_x += 1
            else:
                self.rect.right = WIDTH

        if self.rect.y < 0:
            if self.map_y > 1:
                self.rect.y = HEIGHT
                self.again = 1
                self.map_y += 1
            else:
                self.rect.right = WIDTH

        if self.rect.bottom > HEIGHT:
            if self.map_y < 5:
                self.rect.y = 0
                self.map_y -= 1
                self.again = 1
            else:
                self.rect.bottom = HEIGHT

        prev_keystate = keystate
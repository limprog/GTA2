import pygame
import random
import os
import time
from constants import *
from sprites.Player import *


class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.speedx = 0
        self.speedy = 0
        self.hp = 20

    def update(self):
        player = Player()

        one_control = random.randint(0, 5)
        if one_control == 1:
            two_control = random.randint(0, 3)
            if two_control == 0:
                self.speedx -= 1
            elif two_control == 1:
                self.speedx += 1
            elif two_control == 2:
                self.speedy -= 1
            elif two_control == 3:
                self.speedy += 1
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        self.a = random.randint(0, 14)
        if self.a == 1:
            self.speedx = 0
            self.speedy = 0

    def moveToRandomPoint(self):
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(0, HEIGHT)

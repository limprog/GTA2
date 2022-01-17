import pygame
import random
import os
import time
from constants import *


class Zombie(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0

    def update(self):

        one_control = random.randint(0,5)
        if one_control == 1:
            two_control = random.randint(0,3)
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
        self.a = random.randint(0,14)
        if  self.a == 1:
            self.speedx = 0
            self.speedy = 0
import pygame
import random
import time
import os
from constants import *
class Cartridges(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 15))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center  = (random.randint(0,WIDTH), random.randint(0, HEIGHT) )
    def moveToRandomPoint(self):
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(0, HEIGHT)
    def update(self):
        pass
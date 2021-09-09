import pygame
import random
import time
import os
from constants import *
class Weapon (pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0,WIDTH), random.randint(0, HEIGHT) )
    def update(self):
        pass
        #if self.new == 1:
            #self.rect.x = random.randint(0,WIDTH)
            #self.rect.y = random.randint(0, HEIGHT)
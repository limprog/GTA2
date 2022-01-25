import pygame
import time
import random
from constants import *
class Ammunition(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 15))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0,HEIGHT))

    def moveToRandomPoint(self):
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(0, HEIGHT)
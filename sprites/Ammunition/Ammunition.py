import pygame
import time
import random
import os
from constants import *


class Ammunition(pygame.sprite.Sprite):
    def __init__(self, texture=None):
        pygame.sprite.Sprite.__init__(self)
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '../../imge/Ammunition/')
        player_img = pygame.image.load(os.path.join(img_folder, texture)).convert()
        self.image = player_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

    def moveToRandomPoint(self):
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(0, HEIGHT)

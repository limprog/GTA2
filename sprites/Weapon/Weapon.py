import pygame
import random
import time
import os
from constants import *


class Weapon(pygame.sprite.Sprite):
    def __init__(self, damage=0, texture=None, clip=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))

        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '../../imge/weapon/')
        player_img = pygame.image.load(os.path.join(img_folder, texture)).convert()

        self.image = player_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.dagame = damage

    def moveToRandomPoint(self):
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(0, HEIGHT)

    def update(self):
        pass

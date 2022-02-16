import pygame
from constants import *
import random
import os
import time


class Pig(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '..\imge')
        player_img = pygame.image.load(os.path.join(img_folder, 'fsh09SH.png')).convert()
        self.image = player_img
        self.image.set_colorkey(WHITE)
        self.image =pygame.transform.scale (self.image,(self.image.get_width() // 2,self.image.get_height() // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.speedx = 0
        self.speedy = 0
        self.hp = 10
        self.updat = 1

    def update(self):
        if self.updat == 1:
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

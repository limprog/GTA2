import pygame
from constants import *


class NLO(pygame.sprite.Sprite):
    def __init__(self, x1, y1, damage, x2, y2):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((6, 6))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (x1, y1)
        self.x2 = x2
        self.y2 = y2
        self.dx = (x2 - x1) / 60
        self.dy = (y2 - y1) / 60

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

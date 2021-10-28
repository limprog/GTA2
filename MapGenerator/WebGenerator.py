import pygame
from constants import *
import random

MATERIALS = {
    'grass' : GREEN,
    'beton' : GRAY

}
SIDESIZE = 120

class WebCell(pygame.sprite.Sprite):
    def __init__(self,  x, y, material='grass'):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIDESIZE, SIDESIZE))
        self.image.fill(MATERIALS[material])
        self.rect =self.image.get_rect()
        self.rect.center = (x+SIDESIZE//2, y+SIDESIZE//2)
        # print(self.rect.x, self.rect.y)


class WebGenerator:
    def __init__(self):
        self.number_vert_cell = HEIGHT // SIDESIZE
        self.number_hor_cell = WIDTH // SIDESIZE
    def createWeb(self):
        self.web = [[None]*self.number_hor_cell]*self.number_vert_cell
        for i in range(self.number_vert_cell):
            for j in range(self.number_hor_cell):
                self.web[i][j] = WebCell(j*SIDESIZE, i*SIDESIZE, random.choice(list(MATERIALS.keys())))
        return self.web

import pygame
from constants import *
import random
from sprites.Player import *

MATERIALS = {
    'grass' : DARKGREEN,
    'beton' : GRAY,


}
SIDESIZE = 120

class WebCell(pygame.sprite.Sprite):
    def __init__(self,  x, y, material='grass'):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIDESIZE, SIDESIZE))
        self.image.fill(MATERIALS[material])
        self.rect =self.image.get_rect()
        self.rect.center = (x+SIDESIZE//2, y+SIDESIZE//2)
        #print("webcell", self.rect.x, self.rect.y)


class WebGenerator:
    def __init__(self):
        self.number_vert_cell = HEIGHT // SIDESIZE
        self.number_hor_cell = WIDTH // SIDESIZE
        self.web = None
    @property
    def createWeb(self):
        self.web = [[0 for _ in range(self.number_hor_cell)] for _ in range(self.number_vert_cell)]
        for a in range(self.number_vert_cell):
            for b in range(self.number_hor_cell):
                self.web[a][b] = WebCell(b*SIDESIZE, a*SIDESIZE, random.choice(list(MATERIALS.keys())))

        return self.web
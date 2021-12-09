import pygame
from constants import *
import random


MATERIALS = {
    'grass' : DARKGREEN,
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
        #print("webcell", self.rect.x, self.rect.y)


class WebGenerator:
    def __init__(self):
        self.number_vert_cell = HEIGHT // SIDESIZE
        self.number_hor_cell = WIDTH // SIDESIZE
    @property
    def createWeb(self):
        self.web = []
        for x in range(11):
            self.web.append([int(y) for y in range(4)])
        self.web = [[None]*self.number_hor_cell]*self.number_vert_cell
        webtest= [[(i, j) for j in range(self.number_hor_cell)] for i in range(self.number_vert_cell)]

        for i in range(self.number_vert_cell):
            for j in range(self.number_hor_cell):
                print(webtest[i][j])

        for a in range(self.number_vert_cell):
            for b in range(self.number_hor_cell):
                self.web[a][b] = WebCell(b*SIDESIZE, a*SIDESIZE, random.choice(list(MATERIALS.keys())))
                webtest[a][b] = (b * SIDESIZE, a * SIDESIZE)
        # for i in self.web:
        #     for j in i:
        #         pass
        #         #print(j.rect.y, j.rect.x)
        return self.web
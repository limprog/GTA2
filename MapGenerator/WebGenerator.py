import pygame
from constants import *
import random
from sprites.Player import *

SIDESIZE = 60
class Bioms_generator:
    def __init__(self):
        self.bioms = ["пустыня","лес","город", "болото"]
        self.bioms_cei = "город"
        self.MATERIALS = {'land': DARKGRAY,'road': GRAY,'water': DARKGRAY}
        self.g = 0
        self.change = 0
    def bioms_vibir(self):
        if self.g == 0:
            self.g = 1
        else:
            self.change = random.randint(0,1)
            if self.change == 1:
                self.bioms_cei = random.choice(self.bioms)
                if self.bioms_cei == "город":
                    self.MATERIALS = {'land': DARKGRAY,'road': GRAY, 'water' : DARKGRAY}
                elif self.bioms_cei == "лес":
                    self.MATERIALS = {'land': DARKGREEN,'road': BROWN, 'water' : BLUE}
                elif self.bioms_cei == "пустыня":
                    self.MATERIALS = {'land': YELLOW,'road':ORANGE, 'water' : YELLOW}
                elif self.bioms_cei == "болото":
                    self.MATERIALS = {'land': DARKDARKGREEN,'road': DARKDARKGREEN, 'water' : DARKGREEN}




bioms_generator = Bioms_generator()

class WebCell(pygame.sprite.Sprite):
    def __init__(self,  x, y, material='land'):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIDESIZE, SIDESIZE))
        self.image.fill(material)
        self.rect = self.image.get_rect()
        self.rect.center = (x+SIDESIZE//2, y+SIDESIZE//2)
        #print("webcell", self.rect.x, self.rect.y)


class WebGenerator:
    def __init__(self):
        self.number_vert_cell = HEIGHT // SIDESIZE
        self.number_hor_cell = WIDTH // SIDESIZE
        self.web = None
    @property
    def createWeb(self):
        bioms_generator.bioms_vibir()
        self.web = [[0 for _ in range(self.number_hor_cell)] for _ in range(self.number_vert_cell)]
        for a in range(self.number_vert_cell):
            for b in range(self.number_hor_cell):
                material = random.choice(list(bioms_generator.MATERIALS.keys()))
                self.web[a][b] = WebCell(b*SIDESIZE, a*SIDESIZE,bioms_generator.MATERIALS[material])

        return self.web
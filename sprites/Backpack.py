import pygame
from sprites.Player import *
from sprites.Weapon import *
from sprites.Cartridges import *
class Backpack:
    def __init__(self):
        self.weapon = Weapon()
        self.сartridges = Cartridges()
        self.сartridges_group = pygame.sprite.Group()
        self.weapon_group = pygame.sprite.Group()
        self.сartridges_group.add(self.сartridges)
        self.weapon_group.add(self.weapon)

    def get_catriges(self):
        return self.сartridges_group

    def get_weapons(self):
        return self.weapon_group

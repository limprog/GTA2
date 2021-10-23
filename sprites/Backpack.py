from sprites.Player import *
from sprites.Weapon.Weapon import *
from sprites.Cartridges import *
class Backpack:
    def __init__(self):
        self.weapon = Weapon()
        self.сartridges = Cartridges()
        self.сartridges_group = pygame.sprite.Group()
        self.weapon_group = pygame.sprite.Group()
        self.сartridges_group.add(self.сartridges)
        self.weapon_group.add(self.weapon)

from sprites.Player import *
from sprites.Weapon.Weapon import *
from sprites.Cartridges import *
from sprites.Weapon.firearms import *


class Backpack:
    def __init__(self):
        self.weapon = Gun()
        self.сartridges = Cartridges()
        self.сartridges_group = pygame.sprite.Group()
        self.weapon_group = pygame.sprite.Group()
        self.сartridges_group.add(self.сartridges)
        self.weapon_group.add(self.weapon)

    def Random_weapon(self):
        weapons = [Gun(), Сrossbow(), Shotgun(), Kalash(),Revolver(),Ultrasound()]
        self.weapon = random.choice(weapons)
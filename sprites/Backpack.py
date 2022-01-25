from sprites.Cartridges import *
from sprites.Weapon.firearms import *
from sprites.Ammunition.ammunitions import *


class Backpack:
    def __init__(self):
        self.weapon = Gun()
        self.сartridges = Cartridges()
        self.ammunition = Helmet1()
        self.nlo_group = pygame.sprite.Group()
        self.сartridges_group = pygame.sprite.Group()
        self.weapon_group = pygame.sprite.Group()
        self.ammunition_group = pygame.sprite.Group()
        self.сartridges_group.add(self.сartridges)
        self.weapon_group.add(self.weapon)
        self.ammunition_group.add(self.ammunition)

    def Random_weapon(self):
        weapons = [Gun(), Сrossbow(), Shotgun(), Kalash(),Revolver(),Ultrasound()]
        self.weapon = random.choice(weapons)
    def Random_ammunitions(self):
        ammunitions = [Helmet1(), Helmet2(), Helmet3(), Bib1(), Bib2()]
        self.ammunition = random.choice(ammunitions)
import pygame
import random
import time
import os
from constants import *
from ..Inventory import Equipable


class Weapon(Equipable):
    def __init__(self, damage=0, texture=None, clip=0, atk=0, wpn_type=None):
        Equipable.__init__(self, texture, damage)
        self.image = pygame.Surface((25, 25))

        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '../../imge/weapon/')
        player_img = pygame.image.load(os.path.join(img_folder, texture)).convert()

        self.image = player_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.damage = damage
        self.atk = atk
        self.slot = 'weapon'
        self.wpn_type = wpn_type

    def moveToRandomPoint(self):
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(0, HEIGHT)

    def update(self):
        pass

    def equip(self, inv, target):
        if inv.getEquipSlot(self).item != None:
            inv.getEquipSlot(self).item.unequip(inv)
        Equipable.equip(self, target)
        target.equip_weapon(self)
        inv.removeItemInv(self)
        inv.getEquipSlot(self).item = self

    def unequip(self, inv):
        self.equipped_to.unequip_weapon()
        Equipable.unequip(self)
        inv.addItemInv(self)
        inv.getEquipSlot(self).item = None
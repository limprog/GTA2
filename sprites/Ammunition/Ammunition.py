import pygame
import time
import random
import os
from constants import *
from ..Inventory import Equipable

class Ammunition(Equipable):
    def __init__(self, texture=None, value=0, prot=0, slot=0):
        Equipable.__init__(self, texture, value)

        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, '../../imge/Ammunition/')
        player_img = pygame.image.load(os.path.join(img_folder, texture)).convert()
        self.image = player_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.prot = prot
        self.slot = slot

    def moveToRandomPoint(self):
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(0, HEIGHT)

    def equip(self, inv, target):
        if inv.getEquipSlot(self).item != None:
            inv.getEquipSlot(self).item.unequip(inv)
        Equipable.equip(self, target)
        target.equip_armor(self)
        inv.removeItemInv(self)
        inv.getEquipSlot(self).item = self


    def unequip(self, inv):
        self.equipped_to.unequip_armor(self.slot)
        Equipable.unequip(self)
        inv.addItemInv(self)
        inv.getEquipSlot(self).item = None

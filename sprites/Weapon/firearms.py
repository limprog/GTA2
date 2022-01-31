import pygame
import time
import random
import os
from sprites.Weapon.Weapon import *


class Gun(Weapon):
    def __init__(self):
        super().__init__(damage=3, texture='оружие_03.png', clip=7, atk=7)


class Сrossbow(Weapon):
    def __init__(self):
        super().__init__(damage=5, texture='оружие_01.png', clip=1, atk=1)


class Shotgun(Weapon):
    def __init__(self):
        super().__init__(damage=10, texture='оружие_06.png', clip=2, atk=2)


class Kalash(Weapon):
    def __init__(self):
        super().__init__(damage=7, texture='оружие_12.png', clip=30, atk=30)


class Revolver(Weapon):
    def __init__(self):
        super().__init__(damage=5, texture='оружие_10.png', clip=5, atk=5)


class Ultrasound(Weapon):
    def __init__(self):
        super().__init__(damage=5, texture='оружие_11.png', clip=30, atk=30)

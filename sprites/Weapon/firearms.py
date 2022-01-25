import pygame
import time
import random
import os
from sprites.Weapon.Weapon import *
class Gun(Weapon):
    def __init__(self):
        super().__init__(damage=3, texture='оружие_03.png')


class Сrossbow(Weapon):
    def __init__(self):
        super().__init__(damage=5, texture='оружие_01.png')


class Shotgun(Weapon):
    def __init__(self):
        super().__init__(damage=10, texture='оружие_06.png')


class Kalash(Weapon):
    def __init__(self):
        super().__init__(damage=7, texture='оружие_12.png')


class Revolver(Weapon):
    def __init__(self):
        super().__init__(damage=5, texture='оружие_10.png')


class Ultrasound(Weapon):
    def __init__(self):
        super().__init__(damage=5, texture='оружие_11.png')


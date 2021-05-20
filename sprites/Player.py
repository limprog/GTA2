from game import *
from constants import *
import pygame
import time
'''
Класс, описывающий сущность игрока
'''
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a] or keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_LSHIFT] and (keystate[pygame.K_a] or keystate[pygame.K_LEFT]):
            self.speedx = -14

        if keystate[pygame.K_d] or keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_LSHIFT] and (keystate[pygame.K_d] or keystate[pygame.K_RIGHT]):
            self.speedx = 14

        if keystate[pygame.K_w] or keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_LSHIFT] and (keystate[pygame.K_w] or keystate[pygame.K_UP]):
            self.speedy = -14

        if keystate[pygame.K_s] or keystate[pygame.K_DOWN]:
            self.speedy = 8
        if keystate[pygame.K_LSHIFT] and (keystate[pygame.K_s] or keystate[pygame.K_DOWN]):
            self.speedx = -14

        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


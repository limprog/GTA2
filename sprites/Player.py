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
        self.speedx = 0
        self.speedy = 0

    def translateMovement(self, keystate):
        key_dict = {'left':keystate[pygame.K_a] or keystate[pygame.K_LEFT], 'up':keystate[pygame.K_w] or keystate[pygame.K_UP],
                    "right":keystate[pygame.K_d] or keystate[pygame.K_RIGHT], 'down':keystate[pygame.K_s] or keystate[pygame.K_DOWN]}
        return key_dict

    def update(self):
        keystate = self.translateMovement(pygame.key.get_pressed())
        abs_speed = 8
        if keystate['left']:
            self.speedx -= 0.1
            if self.speedx <= -abs_speed:
                self.speedx = -abs_speed

        if keystate['right']:
            self.speedx += 0.1
            if self.speedx >= abs_speed:
                self.speedx = abs_speed

        if keystate['down']:
            self.speedy += 0.1
            if self.speedy <= -abs_speed:
                self.speedy = -abs_speed

        if keystate['up']:
            self.speedy -= 0.1
            if self.speedy >= abs_speed:
                self.speedy = abs_speed

        if all(v==0 for v in keystate.values()):
            if self.speedx <= -0.2:
                self.speedx += 0.2
            elif self.speedx >= 0.2:
                self.speedx -= 0.2
            else:
                self.speedx = 0
            if self.speedy <= -0.2:
                self.speedy += 0.2
            elif self.speedy >= 0.2:
                self.speedy -= 0.2
            else:
                self.speedy = 0

        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            #self.rect.right = WIDTH
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = WIDTH - 50
            #self.rect.x =
        if self.rect.y <= 0:
            self.rect.y = HEIGHT - 50
        if self.rect.bottom > HEIGHT:
            self.rect.y = 0
        prev_keystate = keystate

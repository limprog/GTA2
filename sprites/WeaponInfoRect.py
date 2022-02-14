import pygame

class WeaponInfoRect():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        rect1 = pygame.Rect((x, y, 200, 100))
        font = pygame.font.Font(None, 25)
        self.text = ""
        text_renderer = font.render("You win!", True, (0, 0, 0))

    def update(self, text):
        self.text = text

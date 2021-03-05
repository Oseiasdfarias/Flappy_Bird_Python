import pygame
from pygame.locals import *

SPEED_GAME = 10

class Base(pygame.sprite.Sprite):

    def __init__(self, width, height_display, height, xpos):
        pygame.sprite.Sprite.__init__(self)
        
        self.width = width
        self.height = height
        self.height_display = height_display
        self.xpos = xpos

        self.image = pygame.image.load("animation/base.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = height_display - height

    def update(self):
        self.rect[0] -= SPEED_GAME

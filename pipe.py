import pygame
from pygame.locals import *

SPEED_GAME = 10
PIPE_WIDTH = 75
PIPE_HEIGHT = 500

class Pipe(pygame.sprite.Sprite):
    def __init__(self, inverted, xpos, y_size, display_height):
        pygame.sprite.Sprite.__init__(self)

        self.xpos = xpos
        self.y_size = y_size
        self.display_height = display_height

        self.image = pygame.image.load("animation/pipe-red.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos

        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = - (self.rect[3] - y_size)
        else:
            self.rect[1] = display_height - y_size
        
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect[0] -= SPEED_GAME

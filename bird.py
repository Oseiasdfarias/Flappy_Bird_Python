import pygame
from pygame.locals import *

SPEED_BIRD = 10
GRAVIRY = 1

class Bird(pygame.sprite.Sprite):
    def __init__(self, width, heigth):
        pygame.sprite.Sprite.__init__(self)

        self.width = width
        self.height = heigth
        
        self.images = [
        pygame.image.load("animation/bluebird-upflap.png").convert_alpha(),
        pygame.image.load("animation/bluebird-midflap.png").convert_alpha(),
        pygame.image.load("animation/bluebird-downflap.png").convert_alpha()
        ]

        self.speed = SPEED_BIRD

        self.current_image = 0

        self.image = pygame.image.load("animation/bluebird-upflap.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.image = pygame.transform.scale(self.image, (int(34*2), int(24*2)))
        self.rect = self.image.get_rect()
        self.rect[0] = (width / 2) - 20
        self.rect[1] = (heigth / 2) - 40


    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]

        self.speed += GRAVIRY

        # Update height
        self.rect[1] += self.speed

    def jump(self):
        self.speed = -SPEED_BIRD

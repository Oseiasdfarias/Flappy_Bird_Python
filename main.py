#!/usr/bin/env python3

import pygame, random
from pygame.locals import *
from bird import Bird
from base import Base
from pipe import Pipe
from time import sleep


DISPLAY_WIDTH = 400
DISPLAY_HEIGHT = 660

BASE_WIDTH = 2 * DISPLAY_WIDTH
BASE_HEIGHT = 100

PIPE_GAP = 180

pygame.font.init()

STAT_FONT = pygame.font.SysFont("comicsans", 35)

pygame.init()
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

BG_DISPLAY = pygame.image.load("animation/background-day.png")
BG_DISPLAY = pygame.transform.scale(BG_DISPLAY, (DISPLAY_WIDTH, DISPLAY_HEIGHT))

bird_group = pygame.sprite.Group()
bird = Bird(width=DISPLAY_WIDTH, heigth=DISPLAY_HEIGHT)
bird_group.add(bird)

def get_random_pipes(xpos):
    size = random.randint(100, 300)
    pipe = Pipe(False, xpos, (2 + size), DISPLAY_HEIGHT)
    pipe_inverted = Pipe(True, xpos, DISPLAY_HEIGHT - size - PIPE_GAP, DISPLAY_HEIGHT)

    return (pipe, pipe_inverted)

def display_off(sprite):
    return sprite.rect[0] < -(sprite.rect[2])


base_group = pygame.sprite.Group()
for i in range(2):
    base = Base(BASE_WIDTH, DISPLAY_HEIGHT, BASE_HEIGHT, (BASE_WIDTH * i)-5 )
    base_group.add(base)

pipe_group = pygame.sprite.Group()
for i in range(2):
    pipes = get_random_pipes(DISPLAY_WIDTH * i + 800)
    pipe_group.add(pipes[0])
    pipe_group.add(pipes[1])

if __name__ == "__main__":

    gameLoop = True
    gameOver = False
    clock = pygame.time.Clock()

    while gameLoop:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    bird.jump()

        if not gameOver:

            display.blit(BG_DISPLAY, (0, 0))

            if display_off(base_group.sprites()[0]):
                base_group.remove(base_group.sprites()[0])

                new_base = Base(BASE_WIDTH, DISPLAY_HEIGHT, BASE_HEIGHT, (BASE_WIDTH * i)-5)
                base_group.add(new_base)

            if display_off(pipe_group.sprites()[0]):
                pipe_group.remove(pipe_group.sprites()[0])
                pipe_group.remove(pipe_group.sprites()[0])

                pipes = get_random_pipes(DISPLAY_WIDTH * 2)

                pipe_group.add(pipes[0])
                pipe_group.add(pipes[1])


            bird_group.update()
            base_group.update()
            pipe_group.update()

            bird_group.draw(display)
            pipe_group.draw(display)
            base_group.draw(display)


        if (pygame.sprite.groupcollide(bird_group, base_group, False, False, pygame.sprite.collide_mask) or
        pygame.sprite.groupcollide(bird_group, pipe_group, False, False, pygame.sprite.collide_mask)):
            sleep(0.500)
            gameOver = True

        while gameOver:
            display.blit(BG_DISPLAY, (0, 0))
            text = STAT_FONT.render("Game Over ", 2, (255, 0, 0))
            text2 = STAT_FONT.render('Aperte "S" para SAIR', 1, (255, 0, 0))
            text3 = STAT_FONT.render('ou', 1, (255, 0, 0))
            text4 = STAT_FONT.render('"R" para continuar jogando', 1, (255, 0, 0))

            display.blit(text, (280 - 10 - text.get_width(), 260))
            display.blit(text2, (315 - 10 - text2.get_width(), 300))
            display.blit(text3, (215 - 10 - text3.get_width(), 320))
            display.blit(text4, (345 - 10 - text4.get_width(), 340))

            for event in pygame.event.get():        
                if event.type == KEYDOWN:
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if event.key == pygame.K_s:
                        pygame.quit()
                        exit()

                    if event.key == pygame.K_r:
                        bird_group = pygame.sprite.Group()
                        bird = Bird(width=DISPLAY_WIDTH, heigth=DISPLAY_HEIGHT)
                        bird_group.add(bird)
                        base_group = pygame.sprite.Group()

                        for i in range(2):
                            base = Base(BASE_WIDTH, DISPLAY_HEIGHT, BASE_HEIGHT, (BASE_WIDTH * i)-5 )
                            base_group.add(base)

                        pipe_group = pygame.sprite.Group()
                        for i in range(2):
                            pipes = get_random_pipes(DISPLAY_WIDTH * i + 800)
                            pipe_group.add(pipes[0])
                            pipe_group.add(pipes[1])

                        gameOver = False
                pygame.display.update()
                        
        pygame.display.update()

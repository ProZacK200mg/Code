#!/usr/bin/env python

import pygame
import random
from settings import *

WIDTH = 800
HEIGHT = 600
FPS = 60

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (0, 255, 255)

#initalizing pygame and create window.
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

#creating a all sprites group
all_sprites = pygame.sprite.Group()

#Game Loop
running = True
while running:
    #keeps loop running at the right speed
    clock.tick(FPS)
    #process input (events)
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False

    #Update
    all_sprites.update()

    #render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    #after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()

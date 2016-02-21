#!/usr/bin/env python

import pygame as pg
from player import *
from settings import *

class Game:
    def __init__(self):
        #Initialize game window, etc...
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        #Start a new game
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        #Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        #Game Loop - events
            for event in pg.event.get():
                #check for closing window
                if event.type == pg.QUIT:
                    if self.playing:
                        self.playing = False
                    self.running = False

                if event.type == pg.KEYUP:
                    if event.key == pg.K_RIGHT:
                        self.player.vx = 0
                        self.player.image = self.player.right[0]
                    if event.key == pg.K_LEFT:
                        self.player.vx = 0
                        self.player.image = self.player.left[0]
                    if event.key == pg.K_UP:
                        self.player.vy = 0
                        self.player.image = self.player.up[0]
                    if event.key == pg.K_DOWN:
                        self.player.vy = 0
                        self.player.image = self.player.down[0]

    def update(self):
        #Game Loop - update
        self.all_sprites.update()

    def draw(self):
        #Game Loop - draw
            self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)
            # *after* drawing everything, flip the display
            pg.display.flip()

    def show_start_screen(self):
        #Game splash/start screen
        pass

    def show_go_screen(self):
        #Game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()

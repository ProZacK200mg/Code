import pygame as pg
import random
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__ (self)
        self.image = pg.Surface([32, 32])
        self.image.fill(RED)
        self.rect= self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.vx = 0
        self.vy = 0

        ##TODO: Need to make it add files as part of a loop
        ##      so i can save space in code and tpying when i add
        ##      more pictures for up down and right animations
        ##Loading all the img files and putting them into a list
        self.right = []
        self.right.append(pg.image.load("img/right_stand.png"))
        self.right.append(pg.image.load("img/right_2.png"))
        self.right.append(pg.image.load("img/right_3.png"))
        self.right.append(pg.image.load("img/right_4.png"))

        ##Load left image list
        self.left = []
        self.left.append(pg.image.load("img/left_stand.png"))
        self.left.append(pg.image.load("img/left_2.png"))
        self.left.append(pg.image.load("img/left_3.png"))
        self.left.append(pg.image.load("img/left_4.png"))

        ##Load up image list
        self.up = []
        self.up.append(pg.image.load("img/up_stand.png"))
        self.up.append(pg.image.load("img/up_2.png"))
        self.up.append(pg.image.load("img/up_3.png"))
        self.up.append(pg.image.load("img/up_4.png"))

        ##Load down image list
        self.down = []
        self.down.append(pg.image.load("img/down_stand.png"))
        self.down.append(pg.image.load("img/down_2.png"))
        self.down.append(pg.image.load("img/down_3.png"))
        self.down.append(pg.image.load("img/down_4.png"))

        self.frame = 0
        self.image = self.down[self.frame]

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.vx = 5
            ##start right animation
            self.frame +=1
            if self.frame == len(self.right):
                self.frame = 0
            self.image = self.right[self.frame]

        if keys[pg.K_LEFT]:
            self.vx = -5
            ##start left animation
            self.frame +=1
            if self.frame == len(self.left):
                self.frame = 0
            self.image = self.left[self.frame]

        if keys[pg.K_UP]:
            self.vy = -5
            ##start up animation
            self.frame +=1
            if self.frame == len(self.up):
                self.frame = 0
            self.image = self.up[self.frame]

        if keys[pg.K_DOWN]:
            self.vy = 5
            ##start down animation
            self.frame +=1
            if self.frame == len(self.down):
                self.frame = 0
            self.image = self.down[self.frame]

        self.rect.x += self.vx
        self.rect.y += self.vy

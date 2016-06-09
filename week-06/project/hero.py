from tkinter import *
import random

class Hero(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.hero_down_image = PhotoImage(file='hero-down.png')
        self.hero_left_image = PhotoImage(file='hero-left.png')
        self.hero_right_image = PhotoImage(file='hero-right.png')
        self.hero_up_image = PhotoImage(file='hero-up.png')
        self.x = 1
        self.y = 1
        self.level_of_hero = 1
        self.max_hp = 20 + 3 * random.randint(1, 6)
        self.hp = self.max_hp
        self.dp = 2 * random.randint(1, 6)
        self.sp = 5 + random.randint(1, 6)
        self.draw_hero(self.hero_down_image)

    def stat(self):
        stat = 'Hero (Level 1) HP: ' + str(self.hp) + '/' + str(self.max_hp) + ' | DP: ' + str(self.dp) + ' | SP: ' + str(self.sp)
        return stat

    def draw_hero(self, hero_direction):
        self.canvas.create_image(self.x*60-53, self.y*60-53, image = hero_direction, anchor = NW)
        self.canvas.create_text(310, 620, text=self.stat())

    def move_hero(self, x, y):
        self.x += x
        self.y += y

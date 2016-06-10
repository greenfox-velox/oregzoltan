from tkinter import *
import random

class Hero(object):
    def __init__(self, canvas, level):
        self.canvas = canvas
        self.level = level
        self.hero_direction_image = PhotoImage(file='hero-down.png')
        self.x = 1
        self.y = 1
        self.max_hp = 20 + 3 * random.randint(1, 6)
        self.hp = self.max_hp
        self.dp = 2 * random.randint(1, 6)
        self.sp = 5 + random.randint(1, 6)
        self.draw_hero()
        self.is_boss_killed = False
        self.has_the_key = False

    def stat(self):
        stat = 'Hero (Level ' + str(self.level) + ') HP: ' + str(self.hp) + '/' + str(self.max_hp) + ' | DP: ' + str(self.dp) + ' | SP: ' + str(self.sp)
        return stat

    def draw_hero(self):
        self.canvas.create_image(self.x*60-53, self.y*60-53, image = self.hero_direction_image, anchor = NW)
        self.canvas.create_text(310, 620, text=self.stat())

    def set_hero_direction_image(self, direction):
        if direction == 'up':
            self.hero_direction_image = PhotoImage(file='hero-up.png')
        elif direction == 'down':
            self.hero_direction_image = PhotoImage(file='hero-down.png')
        elif direction == 'right':
            self.hero_direction_image = PhotoImage(file='hero-right.png')
        elif direction == 'left':
            self.hero_direction_image = PhotoImage(file='hero-left.png')

    def move_hero(self, x, y):
        self.x += x
        self.y += y

    def level_up_hero(self):
        self.max_hp += random.randint(1, 6)
        self.dp += random.randint(1, 6)
        self.sp += random.randint(1, 6)

    def hero_to_next_area(self, save_hero_hp, save_hero_max_hp):
        ran = random.randint(1, 10)
        if ran == 1:
            self.hp = save_hero_max_hp
        elif ran >= 2 and ran <=5 :
            self.hp = save_hero_hp + save_hero_hp//3
        else:
            self.hp = save_hero_hp + save_hero_hp//10
        self.max_hp = save_hero_max_hp
        if self.hp > self.max_hp:
            self.hp = self.max_hp

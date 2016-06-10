import random
from tkinter import *

class Monster(object):
    def __init__(self, x, y, canvas):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.key = False

class Skeleton(Monster):
    def __init__(self, x, y, canvas, level):
        super().__init__(x, y, canvas)
        self.skeleton_image = PhotoImage(file='skeleton.png')
        self.boss = False
        self.max_hp = 2 * level * random.randint(1, 6)
        self.hp = self.max_hp
        self.dp = level/2 * random.randint(1, 6)
        self.sp = level * random.randint(1, 6)

    def stat(self):
        stat =  'Monster HP: ' + str(self.hp) + '/' + str(self.max_hp) + ' | DP: ' + str(self.dp) + ' | SP: ' + str(self.sp)
        if self.key == True:
            stat += ' I have the key'
        return stat

    def draw(self):
        self.canvas.create_image(self.x*60-53, self.y*60-53, image = self.skeleton_image, anchor = NW)

class Boss(Monster):
    def __init__(self, x, y, canvas, level):
        super().__init__(x, y, canvas)
        self.boss_image = PhotoImage(file='boss.png')
        self.boss = True
        self.max_hp = 2 * level * random.randint(1, 6) + random.randint(1, 6)
        self.hp = self.max_hp
        self.dp = level/2 * random.randint(1, 6) + random.randint(1, 6)/2
        self.sp = level *  random.randint(1, 6) + level

    def stat(self):
        stat = 'Boss HP: ' + str(self.hp) + '/' + str(self.max_hp) + ' | DP: ' + str(self.dp) + ' | SP: ' + str(self.sp)
        return stat

    def draw(self):
        self.canvas.create_image(self.x*60-53, self.y*60-53, image = self.boss_image, anchor = NW)

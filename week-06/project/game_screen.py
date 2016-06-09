from tkinter import *
import random
from monsters import *
from hero import Hero

class Floor(object):
    def __init__(self, x, y, canvas):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.floor_image = PhotoImage(file='floor.png')
        self.type = 'floor'
        self.enemy = False

    def draw(self):
        self.canvas.create_image(self.x*60-53, self.y*60-53, image = self.floor_image, anchor = NW)

class Wall(object):
    def __init__(self, x, y, canvas):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.wall_image = PhotoImage(file='wall.png')
        self.type = 'wall'

    def draw(self):
        self.canvas.create_image(self.x*60-53, self.y*60-53, image = self.wall_image, anchor = NW)

class Tile(object):
    def __init__(self, canvas):
        self.map = []
        self.create_tiles(canvas)

    def create_tiles(self, canvas):
        for x in range(1, 11):
            for y in range(1, 11):
                if x == 1 and y == 1:
                    self.map.append(Floor(1, 1, canvas))
                else:
                    ran = random.randint(1, 10)
                    if ran < 5 and x > 1 and x < 10 and y > 1 and y < 10:
                        self.map.append(Wall(x, y, canvas))
                    else:
                        self.map.append(Floor(x, y, canvas))

class GameScreen(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.tile = Tile(canvas)
        self.create_monsters()
        self.draw_map()
        self.hero = Hero(canvas)

    def create_monsters(self):
        self.monsters = []
        for i in range(4):
            j = True
            while j == True:
                ran_x = random.randint(2, 10)
                ran_y = random.randint(2, 10)
                for each in self.tile.map:
                    if each.x == ran_x and each.y == ran_y and each.type == 'floor' and each.enemy == False:
                        if i == 0:
                            self.monsters.append(Boss(ran_x, ran_y, self.canvas))
                        elif i == 1:
                            self.monsters.append(Skeleton(ran_x, ran_y, self.canvas))
                            self.monsters[1].key = True
                        else:
                            self.monsters.append(Skeleton(ran_x, ran_y, self.canvas))
                            each.enemy = True
                        j = False

    def position_hero_with_check(self, event):
        self.draw_map()
        if event.keysym == 'Down':
            for each in self.tile.map:
                if each.x == self.hero.x and each.y == self.hero.y+1 and each.type != 'wall' and self.hero.y+1 <= 10:
                    self.hero.move_hero(0, 1)
                    break
            self.hero.draw_hero(self.hero.hero_down_image)

        if event.keysym == 'Up':
            for each in self.tile.map:
                if each.x == self.hero.x and each.y == self.hero.y-1 and each.type != 'wall' and self.hero.y-1 >= 1:
                    self.hero.move_hero(0, -1)
            self.hero.draw_hero(self.hero.hero_up_image)

        if event.keysym == 'Left':
            for each in self.tile.map:
                if each.x == self.hero.x-1 and each.y == self.hero.y and each.type != 'wall' and self.hero.x-1 >= 1:
                    self.hero.move_hero(-1, 0)
            self.hero.draw_hero(self.hero.hero_left_image)

        if event.keysym == 'Right':
            for each in self.tile.map:
                if each.x == self.hero.x+1 and each.y == self.hero.y and each.type != 'wall' and self.hero.x+1 <= 10:
                    self.hero.move_hero(1, 0)
                    break
            self.hero.draw_hero(self.hero.hero_right_image)

        self.hero_vs_monster()

    def draw_map(self):
        self.canvas.delete('all')
        for field in self.tile.map:
            field.draw()
        for each in self.monsters:
            each.draw()

    def hero_vs_monster(self):
        for each in self.monsters:
            if each.x == self.hero.x and each.y == self.hero.y:
                self.canvas.create_text(300, 640, text=each.stat())

from tkinter import *
import random
from monsters import *
from hero import Hero
import sys

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

class Board(object):
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
        self.level = 1
        self.step_counter = 0
        self.canvas = canvas
        self.board = Board(canvas)
        self.create_monsters()
        self.hero = Hero(canvas, self.level)
        self.draw_map()

    def create_monsters(self):
        self.monsters = []
        for i in range(random.randint(4, 7)):
            j = True
            while j == True:
                ran_x = random.randint(2, 10)
                ran_y = random.randint(2, 10)
                for tile in self.board.map:
                    if tile.x == ran_x and tile.y == ran_y and tile.type == 'floor' and tile.enemy == False:
                        if i == 0:
                            self.monsters.append(Boss(ran_x, ran_y, self.canvas, self.level))
                        elif i == 1:
                            self.monsters.append(Skeleton(ran_x, ran_y, self.canvas, self.level))
                            self.monsters[1].key = True
                        else:
                            self.monsters.append(Skeleton(ran_x, ran_y, self.canvas, self.level))
                        tile.enemy = True
                        j = False

    def position_hero_with_check(self, event):
        if event.keysym == 'Down':
            for tile in self.board.map:
                if tile.x == self.hero.x and tile.y == self.hero.y+1 and tile.type != 'wall' and self.hero.y+1 <= 10:
                    self.hero.move_hero(0, 1)
                    break
            self.hero.set_hero_direction_image('down')
            self.step_counter += 1

        if event.keysym == 'Up':
            for tile in self.board.map:
                if tile.x == self.hero.x and tile.y == self.hero.y-1 and tile.type != 'wall' and self.hero.y-1 >= 1:
                    self.hero.move_hero(0, -1)
            self.hero.set_hero_direction_image('up')
            self.step_counter += 1

        if event.keysym == 'Left':
            for tile in self.board.map:
                if tile.x == self.hero.x-1 and tile.y == self.hero.y and tile.type != 'wall' and self.hero.x-1 >= 1:
                    self.hero.move_hero(-1, 0)
            self.hero.set_hero_direction_image('left')
            self.step_counter += 1

        if event.keysym == 'Right':
            for tile in self.board.map:
                if tile.x == self.hero.x+1 and tile.y == self.hero.y and tile.type != 'wall' and self.hero.x+1 <= 10:
                    self.hero.move_hero(1, 0)
                    break
            self.hero.set_hero_direction_image('right')
            self.step_counter += 1

        if event.keysym == 'space':
            counter = -1
            for monster in self.monsters:
                counter += 1
                if monster.x == self.hero.x and monster.y == self.hero.y:
                    self.battle(monster, counter)

        if event.keysym == 'Escape':
            self.hero_dies()

        if event.keysym == 'n':
            self.next_area()
        self.position_checker_to_move_monsters()
        self.draw_map()

    def draw_map(self):
        self.canvas.delete('all')
        for field in self.board.map:
            field.draw()
        for monster in self.monsters:
            monster.draw(self.hero.x, self.hero.y)
        self.hero.draw_hero()

    def battle(self, monster, counter):
        sv = self.hero.sp + random.randint(1, 6)*2
        if sv > monster.dp:
            monster.hp = monster.hp - sv - monster.dp
        if self.hero.hp > 0 and monster.hp > 0:
            sv = monster.sp + random.randint(1, 6)*2
            if sv > self.hero.dp:
                self.hero.hp = self.hero.hp - sv - self.hero.dp
        if self.hero.hp >= 0 and monster.hp <= 0:
            self.hero.level_up_hero()
            if monster.key:
                self.hero.has_the_key = True
            if monster.boss:
                self.hero.is_boss_killed = True
            del self.monsters[counter]
        if self.hero.has_the_key and self.hero.is_boss_killed:
            self.next_area()
        if self.hero.hp <= 0:
            self.hero_dies()
        self.draw_map()

    def next_area(self):
        self.level += 1
        save_hero_hp = self.hero.hp
        save_hero_max_hp = self.hero.max_hp
        self.board = Board(self.canvas)
        self.create_monsters()
        self.draw_map()
        self.hero = Hero(self.canvas, self.level)
        self.hero.hero_to_next_area(save_hero_hp, save_hero_max_hp)

    def hero_dies(self):
        self.canvas.create_text(300, 640, text='GAME OVER')
        self.canvas.after(2000)
        print('game over')
        sys.exit()

    def position_checker_to_move_monsters(self):
        for monster in self.monsters:
            new_position_list = []
            if self.step_counter % 2 == 0:
                for tile in self.board.map:
                    if tile.x == monster.x and tile.y == monster.y-1 and tile.type != 'wall':
                        new_position_list.append([tile.x, tile.y])
                    if tile.x == monster.x and tile.y == monster.y+1 and tile.type != 'wall':
                        new_position_list.append([tile.x, tile.y])
                    if tile.x == monster.x-1 and tile.y == monster.y and tile.type != 'wall':
                        new_position_list.append([tile.x, tile.y])
                    if tile.x == monster.x+1 and tile.y == monster.y and tile.type != 'wall':
                        new_position_list.append([tile.x, tile.y])
                if len(new_position_list) > 0:
                    ran = random.randint(0, len(new_position_list)-1)
                    monster.x = new_position_list[ran][0]
                    monster.y = new_position_list[ran][1]

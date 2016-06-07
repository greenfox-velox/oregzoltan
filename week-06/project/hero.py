from tkinter import *
from game_screen import GameScreen

class Hero(object):
    def __init__(self, canvas, hero_down_image, hero_left_image, hero_right_image, hero_up_image):
        self.canvas = canvas
        self.hero_down_image = hero_down_image
        self.hero_left_image = hero_left_image
        self.hero_right_image = hero_right_image
        self.hero_up_image = hero_up_image
        self.x = 1
        self.y = 1

    def position_hero(self, char, map):
        if char == 'c':
            self.draw_hero(self.hero_down_image)
        if char == '<Down>':
            for each in map:
                if each.x == self.x and each.y == self.y+1 and each.type != 'wall' and self.y+1 <= 10:
                    self.y += 1
                    break
            self.draw_hero(self.hero_down_image)

        if char == '<Up>':
            if self.y-1 >= 1:
                self.y += -1
            self.draw_hero(self.hero_up_image)
        if char == '<Left>':
            if self.x-1 >= 1:
                self.x += -1
            self.draw_hero(self.hero_left_image)
        if char == '<Right>':
            if self.x+1 <= 10:
                self.x += 1
            self.draw_hero(self.hero_right_image)


    def draw_hero(self, hero_direction):
        self.canvas.create_image(self.x*72-65, self.y*72-65, image = hero_direction, anchor = NW)

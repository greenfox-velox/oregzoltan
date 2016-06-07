from tkinter import *
import random

class floor(object):
    def __init__(self, x, y, canvas):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.floor_image = PhotoImage(file='floor.png')
        self.type = 'floor'
    def draw(self):
        self.canvas.create_image(self.x*72-65, self.y*72-65, image = self.floor_image, anchor = NW)

class wall(object):
    def __init__(self, x, y, canvas, wall_image):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.wall_image = wall_image
        self.type = 'wall'
    def draw(self):
        self.canvas.create_image(self.x*72-65, self.y*72-65, image = self.wall_image, anchor = NW)

class GameScreen(object):
    def __init__(self, canvas, wall_image):
        self.canvas = canvas
        self.wall_image = wall_image
        self.map = []
        for x in range(1, 11):
            for y in range(1, 11):
                ran = random.randint(1, 10)
                if ran > 2:
                    self.map.append(floor(x, y, canvas))
                else:
                    self.map.append(wall(x, y, canvas, wall_image))
        self.map.append(floor(1, 1, canvas))

    def draw_map(self):
        for field in self.map:
            field.draw()

# create a 300x300 canvas.
# make it look like a nigth sky:
# - The background should be black
# - The stars can be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

from tkinter import *
import random

root = Tk()

canvas_size = 300
canvas = Canvas(root, bg='black', width=canvas_size, height=canvas_size)
canvas.pack()

def draw_line(x, y, x2, y2, color):
    canvas.create_rectangle(x, y, x2, y2, fill=color)

def randnum():
    r = random.randrange(5, 290)
    return(r)

def random_color():
    r1 = random.randrange(100, 200)
    r2 = random.randrange(100, 200)
    r3 = random.randrange(100, 200)
    r = '#' + str(hex(r1)[2:]) + str(hex(r2)[2:]) + str(hex(r3)[2:])
    return(r)

for i in range(random.randrange(200)):
    x = randnum()
    y = randnum()
    draw_line(x, y, x+3, y+3, random_color())


root.mainloop()

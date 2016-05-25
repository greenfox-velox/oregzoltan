# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_square(size, color):
    x = 300/2-size/2
    draw_box = canvas.create_rectangle(x, x, x+size, x+size, fill=color)

for i in range(300, 1, -1):
    r1 = random.randrange(150, 255)
    r2 = random.randrange(16, 255)
    r3 = random.randrange(16, 150)
    r = '#' + str(hex(r1)[2:]) + str(hex(r2)[2:]) + str(hex(r3)[2:])
    draw_square(i*10, r)
root.mainloop()

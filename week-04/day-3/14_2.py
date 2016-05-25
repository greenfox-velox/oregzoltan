# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r2.png]
# can you make the colors change? make every line a different color.

from tkinter import *
import random

root = Tk()

canvas_size = 300
canvas = Canvas(root, width=canvas_size, height=canvas_size)
canvas.pack()

def draw_line(x, y, x2, y2, color):
    line = canvas.create_line(x, y, x2, y2, fill=color)

def random_color():
    r1 = random.randrange(16, 255)
    r2 = random.randrange(16, 255)
    r3 = random.randrange(16, 255)
    r = '#' + str(hex(r1)[2:]) + str(hex(r2)[2:]) + str(hex(r3)[2:])
    return(r)

for i in range(0, canvas_size//2, 10):
    draw_line(i, canvas_size/2, canvas_size/2, canvas_size/2-i, random_color())
    draw_line(canvas_size-i, canvas_size/2, canvas_size/2, canvas_size/2-i, random_color())
    draw_line(i, canvas_size/2, canvas_size/2, canvas_size/2+i, random_color())
    draw_line(canvas_size-i, canvas_size/2, canvas_size/2, canvas_size/2+i, random_color())

root.mainloop()

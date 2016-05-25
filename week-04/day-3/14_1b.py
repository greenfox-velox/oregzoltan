# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r1.png]
# divide the canvas into 4 parts and repeat the pattern.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_line(x, y, x2, y2):
    black_line = canvas.create_line(x, y, x2, y2, fill=color)

step = 10

for i in range(0, 150, step):
    color = '#87DE8C'
    draw_line(0, i, i, 150)
    draw_line(150, i, 150+i, 150)
    draw_line(0, 150+i, i, 300)
    draw_line(150, 150+i, 150+i, 300)
    color = '#C175F5'
    draw_line(i, 0, 150 , i)
    draw_line(150+i, 0, 300 , i)
    draw_line(i, 150, 150 , 150+i)
    draw_line(150+i, 150, 300 , 150+i)

root.mainloop()

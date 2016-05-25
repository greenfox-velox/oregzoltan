# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_line(x, y):
    black_line = canvas.create_line(x, y, 150, 150, fill='black')

step = 20
for i in range(0, 300, step):
    draw_line(i, 0)
for i in range(0, 300, step):
    draw_line(300, i)
for i in range(300, 0, -step):
    draw_line(i, 300)
for i in range(300, 0, -step):
    draw_line(0, i)
root.mainloop()

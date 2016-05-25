# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_line(x, y):
    green_line = canvas.create_line(x, y, 150, 150, fill='green')

draw_line(10, 15)
draw_line(250, 155)
draw_line(100, 250)
root.mainloop()

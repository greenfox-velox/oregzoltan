# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_square(x, y):
    blue_box = canvas.create_rectangle(x, y, x+50, y+50, fill='blue')

draw_square(10, 10)
draw_square(240, 155)
draw_square(100, 240)
root.mainloop()

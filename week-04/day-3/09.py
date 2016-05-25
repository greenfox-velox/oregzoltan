# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_square(s):
    x = 300/2-s/2
    blue_box = canvas.create_rectangle(x, x, x+s, x+s, fill='blue')

draw_square(80)
draw_square(44)
draw_square(10)
root.mainloop()

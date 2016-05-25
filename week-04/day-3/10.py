# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_square(s):
    x = 300/2-s/2
    blue_box = canvas.create_rectangle(x, x, x+s, x+s, fill='blue')

for i in range(21, 1, -1):
    draw_square(i*10)

root.mainloop()

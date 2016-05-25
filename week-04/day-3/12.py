# create a 300x300 canvas.
# fill it with a checkerboard pattern.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_square(size):
    x = 2
    y = 2
    for i in range(1, 9):
        for j in range(1, 9):
            if (i+j) % 2 == 0:
                color = 'black'
            else:
                color = 'white'
            draw_box = canvas.create_rectangle(x, y, x+size, y+size, fill=color)
            x += size
        x = 2
        y += size

draw_square(300 // 8)

root.mainloop()

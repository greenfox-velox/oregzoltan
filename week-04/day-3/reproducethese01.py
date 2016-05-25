from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_square(size):
    x = 2
    for i in range(1, 20):
        draw_box = canvas.create_rectangle(x, x, x+size, x+size, fill='#B145F3')
        x += size

draw_square(10)

root.mainloop()

from tkinter import *

root = Tk()
w = 602
canvas = Canvas(root, bg='#FEFB00', width=w, height=w)
canvas.pack()

def fractal(x, y, size):
    canvas.create_rectangle(x+size, y, x+size*2, y+size)
    if size <= 5:
        pass
    else:
        s = size // 3
        fractal(x+size, y, s)
        fractal(x+size-s, y+s, s)
        fractal(x+size+s, y+s, s)
        fractal(x+size, y+size-s, s)

canvas.create_rectangle(4, 2, w-4, w-6)
fractal(4, 2, 198)
fractal(4, 398, 198)
fractal(-194, 200, 198)
fractal(202, 200, 198)
root.mainloop()

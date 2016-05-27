from tkinter import *

root = Tk()
w = 620
canvas = Canvas(root, bg='#D9D9D9', width=w, height=w)
canvas.pack()
def draw(x, y, s):
    x1 = x
    y1 = y
    x2 = x+s
    y2 = y
    x3 = s/2+x1
    y3 = 3**0.5*s/2+y1
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="white", outline="black")

def fractal(x, y, s):
    draw(x, y, s)
    s = s/2
    if s <= 5:
        pass
    else:
        fractal(x, y, s)
        fractal(x+s, y, s)
        fractal(x+s/2, 3**0.5*s/2+y, s)

canvas.create_rectangle(2, 2, w, w)
fractal(10, 10, 600)
root.mainloop()

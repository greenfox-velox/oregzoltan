from tkinter import *

root = Tk()
w = 700
h = 550
canvas = Canvas(root, bg='#D9D9D9', width=w, height=h)
canvas.pack()
def draw(x, y, s):
    x1 = x
    y1 = y
    x2 = x+s
    y2 = y
    x3 = x+1.5*s
    y3 = y+3**0.5*s/2
    x4 = x+s
    y4 = y+3**0.5*s
    x5 = x
    y5 = y+3**0.5*s
    x6 = x-s/2
    y6 = y+3**0.5*s/2
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, fill="white", outline="black")

def fractal(x, y, s):
    draw(x, y, s)
    s = s/3
    if s <= 3:
        pass
    else:
        fractal(x, y, s)
        fractal(x+2*s, y, s)
        fractal(x-s, y+3**0.5*s, s)
        fractal(x+3*s, y+3**0.5*s, s)
        fractal(x, y+3**0.5*s*2, s)
        fractal(x+2*s, y+3**0.5*s*2, s)

canvas.create_rectangle(2, 2, w, w)
fractal(195, 10, 300)
root.mainloop()

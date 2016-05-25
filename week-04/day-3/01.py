# create a 300x300 black canvas.
# draw a red horizontal line to its middle.
# draw a green vertical line to its middle.

from tkinter import *

root = Tk()

canvas = Canvas(root, bg='black', width='300', height='300')
canvas.pack()

red_line = canvas.create_line(0, 150, 150, 150, fill='red')
green_line = canvas.create_line(150, 0, 150, 150, fill='green')

root.mainloop()

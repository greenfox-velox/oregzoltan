# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

red_line = canvas.create_line(2, 2, 299, 2, fill='red')
green_line = canvas.create_line(2, 299, 299, 299, fill='green')
yellow_line = canvas.create_line(2, 2, 2, 299, fill='yellow')
blue_line = canvas.create_line(299, 2, 299, 299, fill='blue')

root.mainloop()

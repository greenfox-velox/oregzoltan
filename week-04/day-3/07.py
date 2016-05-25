# create a 300x300 canvas.
# fill it with four different size and color rectangles.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

green_box = canvas.create_rectangle(145, 165, 255, 255, fill='green')
red_box = canvas.create_rectangle(14, 14, 55, 55, fill='red')
blue_box = canvas.create_rectangle(45, 145, 155, 135, fill='blue')
yellow_box = canvas.create_rectangle(125, 85, 155, 105, fill='yellow')

root.mainloop()

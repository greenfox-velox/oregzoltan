# create a 300x300 canvas.
# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_line(list):
    for i in range(len(list)):
        if i<len(list)-1:
            green_line = canvas.create_line(list[i][0], list[i][1], list[i+1][0], list[i+1][1], fill='green')
        else:
            green_line = canvas.create_line(list[i][0], list[i][1], list[0][0], list[0][1], fill='green')

list = [[10, 10], [290,  10], [290, 290], [10, 290]]
draw_line(list)
list = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]
draw_line(list)
root.mainloop()

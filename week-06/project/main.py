from game_screen import GameScreen
from tkinter import *

def main():
    root = Tk()
    canvas = Canvas(root, width=615, height=660)
    canvas.pack()
    game = GameScreen(canvas)
    root.bind('<KeyPress>', game.position_hero_with_check)
    root.mainloop()

main()

from game_screen import GameScreen
from tkinter import *

def main():
    def key_down(event):
        game.position_hero_with_check('<Down>')
    def key_up(event):
        game.position_hero_with_check('<Up>')
    def key_right(event):
        game.position_hero_with_check('<Right>')
    def key_left(event):
        game.position_hero_with_check('<Left>')

    root = Tk()
    canvas = Canvas(root, width=615, height=660)
    canvas.pack()
    game = GameScreen(canvas)

    root.bind_all('<Down>', key_down)
    root.bind_all('<Up>', key_up)
    root.bind_all('<Right>', key_right)
    root.bind_all('<Left>', key_left)
    root.mainloop()

main()

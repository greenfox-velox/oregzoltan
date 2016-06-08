from game_screen import GameScreen
from hero import Hero
from tkinter import *

def main():
    def key_down(event):
        game.draw_map()
        hero.position_hero('<Down>', game.map)
    def key_up(event):
        game.draw_map()
        hero.position_hero('<Up>', game.map)
    def key_right(event):
        game.draw_map()
        hero.position_hero('<Right>', game.map)
    def key_left(event):
        game.draw_map()
        hero.position_hero('<Left>', game.map)

    root = Tk()
    canvas = Canvas(root, width=620, height=660)
    canvas.pack()
    game = GameScreen(canvas)
    hero = Hero(canvas)
    game.draw_map()

    hero.position_hero('create_pos', game.map)
    root.bind_all('<Down>', key_down)
    root.bind_all('<Up>', key_up)
    root.bind_all('<Right>', key_right)
    root.bind_all('<Left>', key_left)
    root.mainloop()

main()

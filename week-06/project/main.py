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
    canvas = Canvas(root, width=750, height=1000)

    wall_image = PhotoImage(file='wall.png')
    hero_down_image = PhotoImage(file='hero-down.png')
    hero_left_image = PhotoImage(file='hero-left.png')
    hero_right_image = PhotoImage(file='hero-right.png')
    hero_up_image = PhotoImage(file='hero-up.png')

    game = GameScreen(canvas, wall_image)
    hero = Hero(canvas, hero_down_image, hero_left_image, hero_right_image, hero_up_image)
    game.draw_map()
    hero.position_hero('c', game.map)
    root.bind_all('<Down>', key_down)
    root.bind_all('<Up>', key_up)
    root.bind_all('<Right>', key_right)
    root.bind_all('<Left>', key_left)
    canvas.pack()
    root.mainloop()

main()

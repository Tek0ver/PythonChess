"""Main file to run PythonChess"""

import pygame as pg
import data.constants as C
from data.game import Game

pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((800, 600))
pg.event.get()

running = True

img_main_menu = pg.image.load(C.img_main_menu).convert()

while running:

    # Limit the framerate to 10 FPS
    clock.tick(10)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            # Leave PythonChess
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                # Leave PythonChess
                running = False
            elif event.key == pg.K_F1:
                # Launch Local PvP
                game = Game(screen, "localpvp")
                pass
            elif event.key == pg.K_F2:
                # Launch Local PvAI
                # TODO:
                pass
            elif event.key == pg.K_F3:
                # Launch Online PvP
                # TODO:
                pass

    screen.blit(img_main_menu, (0, 0))
    pg.display.update()

pg.quit()

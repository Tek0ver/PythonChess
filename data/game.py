"""File with class needed to run PythonChess"""

import pygame as pg
import data.constants as C


class Game:

    def __init__(self, screen, mode):

        self.selection = Selection()

        if mode == "localpvp":
            # TODO: add custom name option
            self.player1 = "Player 1"
            self.player2 = "plaver 2"
        elif mode == "localpvai":
            # TODO:
            pass
        elif mode == "onlinepvp":
            # TODO:
            pass

        self.screen = screen

        # Load image(s)
        self.img_board = pg.image.load(C.img_board).convert()
        self.img_coord = pg.image.load(C.img_coord).convert()
        self.img_coord.set_colorkey((255, 255, 255))

        self.Q = pg.image.load(C.img_Q).convert_alpha()
        self.K = pg.image.load(C.img_K).convert_alpha()
        self.B = pg.image.load(C.img_B).convert_alpha()
        self.H = pg.image.load(C.img_H).convert_alpha()
        self.R = pg.image.load(C.img_R).convert_alpha()
        self.P = pg.image.load(C.img_P).convert_alpha()
        self.q = pg.image.load(C.img_q).convert_alpha()
        self.k = pg.image.load(C.img_k).convert_alpha()
        self.b = pg.image.load(C.img_b).convert_alpha()
        self.h = pg.image.load(C.img_h).convert_alpha()
        self.r = pg.image.load(C.img_r).convert_alpha()
        self.p = pg.image.load(C.img_p).convert_alpha()

        self.grid = [['r', 'h', 'b', 'q', 'k', 'b', 'h', 'r'],
                     ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                     ['0', '0', '0', '0', '0', '0', '0', '0'],
                     ['0', '0', '0', 'r', '0', '0', '0', 'r'],
                     ['0', '0', 'K', '0', 'r', '0', '0', '0'],
                     ['0', '0', '0', '0', '0', '0', '0', '0'],
                     ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                     ['R', 'H', 'B', 'Q', 'K', 'B', 'H', 'R']]

        self.run()

    def run(self):

        running = True

        clock = pg.time.Clock()

        while running:

            # Limit the framerate to 10 FPS
            clock.tick(10)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    # Leave game
                    running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        # Leave game
                        running = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # event.pos = (x, y)
                        # event.button = 1 if left clic
                        self.selection.clic(event.pos, self.grid)

            self.display()

    def display(self):

        self.screen.blit(self.img_board, (0, 0))
        self.screen.blit(self.img_coord, (0, 0))

        self.selection.display(self.screen)

        ind_line = 0
        ind_column = 0
        piece = None

        for line in self.grid:
            for column in line:
                if column == '0':
                    piece = None
                elif column == 'Q':
                    piece = self.Q
                elif column == 'K':
                    piece = self.K
                elif column == 'B':
                    piece = self.B
                elif column == 'H':
                    piece = self.H
                elif column == 'R':
                    piece = self.R
                elif column == 'P':
                    piece = self.P
                elif column == 'q':
                    piece = self.q
                elif column == 'k':
                    piece = self.k
                elif column == 'b':
                    piece = self.b
                elif column == 'h':
                    piece = self.h
                elif column == 'r':
                    piece = self.r
                elif column == 'p':
                    piece = self.p

                if piece is not None:
                    self.screen.blit(
                        piece,
                        (ind_column*C.SPACE+C.PIECES_GRID_OFFSET_X,
                         ind_line*C.SPACE+C.PIECES_GRID_OFFSET_Y))

                ind_column += 1

            ind_line += 1
            ind_column = 0

        pg.display.update()


class Selection:

    def __init__(self):

        self.case = None
        self.img_selected = pg.image.load(C.img_selected).convert_alpha()
        self.img_possible = pg.image.load(C.img_possible).convert_alpha()
        self.active = False
        self.coord_active = (-1, -1)
        self.coords_possible = []

    def display(self, screen):
        if self.active is True:
            screen.blit(self.img_selected, (
                self.coord_active[0] * C.SPACE + C.GRID_OFFSET_X,
                self.coord_active[1] * C.SPACE + C.GRID_OFFSET_Y
            ))
            if self.coords_possible != []:
                for x, y in self.coords_possible:
                    screen.blit(self.img_possible, (
                        x * C.SPACE + C.GRID_OFFSET_X,
                        y * C.SPACE + C.GRID_OFFSET_Y
                        ))

    def clic(self, coord, grid):

        self.coords_possible = []
        self.coord_active = ((int((coord[0] - 29) // C.SPACE)),
                             ((int((coord[1] - 29) // C.SPACE))))
        if self.coord_active[0] in range(8) and \
           self.coord_active[1] in range(8):
            self.active = True

            piece_selected = self.get_piece(
                (self.coord_active[0], self.coord_active[1]), grid)

            if piece_selected in ['R', 'r']:
                # To right
                for x in range(self.coord_active[0]+1, 8):
                    if self.get_piece((x, self.coord_active[1]), grid) != '0':
                        break
                    self.coords_possible.append((x, self.coord_active[1]))
                # To left
                for x in range(self.coord_active[0]-1, -1, -1):
                    if self.get_piece((x, self.coord_active[1]), grid) != '0':
                        break
                    self.coords_possible.append((x, self.coord_active[1]))
                # To up
                for y in range(self.coord_active[1]-1, -1, -1):
                    if self.get_piece((self.coord_active[0], y), grid) != '0':
                        break
                    self.coords_possible.append((self.coord_active[0], y))
                # To down
                for y in range(self.coord_active[1]+1, 8):
                    if self.get_piece((self.coord_active[0], y), grid) != '0':
                        break
                    self.coords_possible.append((self.coord_active[0], y))

        else:
            self.active = False

    def get_piece(self, coord, grid):
        return grid[coord[1]][coord[0]]

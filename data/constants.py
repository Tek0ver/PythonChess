"""Constants to run PythonChess"""

import os

PATH_IMG = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                        'resources', 'images')

WINDOW_SIZE = (800, 600)

# Images
img_main_menu = os.path.join(PATH_IMG, 'menu1.png')
img_board = os.path.join(PATH_IMG, 'board.png')

# Piece images
img_Q = os.path.join(PATH_IMG, 'WQ.png')   # White Queen
img_K = os.path.join(PATH_IMG, 'WK.png')   # White King
img_B = os.path.join(PATH_IMG, 'WB.png')   # White Bishop
img_H = os.path.join(PATH_IMG, 'WH.png')   # White Knight (White Horse)
img_R = os.path.join(PATH_IMG, 'WR.png')   # White Rook
img_P = os.path.join(PATH_IMG, 'WP.png')   # White Pawn

img_q = os.path.join(PATH_IMG, 'BQ.png')   # Black Queen
img_k = os.path.join(PATH_IMG, 'BK.png')   # Black King
img_b = os.path.join(PATH_IMG, 'BB.png')   # Black Bishop
img_h = os.path.join(PATH_IMG, 'BH.png')   # Black Knight (Black Horse)
img_r = os.path.join(PATH_IMG, 'BR.png')   # Black Rook
img_p = os.path.join(PATH_IMG, 'BP.png')   # Black Pawn

# Placement Grid related
SPACE = 67.75
GRID_OFFSET_X = 31
GRID_OFFSET_Y = 31

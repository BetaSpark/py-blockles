"""

This will contain the main game logic behind Blockles. The main class will query this class to figure out how to display the
current state of the game to the player.

"""

import random

class BlocklesGame:

    STRAIGHT_PIECE  = [ [0,5], [1,5], [2,5], [3,5] ]
    RIGHT_L_PIECE   = [ [0,5], [1,5], [2,5], [2,6] ]
    LEFT_L_PIECE    = [ [0,5], [1,5], [2,5], [2,4] ]
    T_PIECE         = [ [0,5], [1,4], [1,5], [1,6] ]
    SQUARE_PIECE    = [ [0,5], [0,6], [1,5], [1,6] ]
    S_PIECE         = [ [0,5], [1,5], [1,4], [0,6] ]
    Z_PIECE         = [ [0,5], [1,5], [0,4], [1,6] ]

    def __init__(self):
        self.board = [['A' for y in range(10)] for x in range(20)]
        self.current_piece = -1
        self.current_coord = [] 

    def generate_piece(self):
        self.current_piece = int(random.random()*7)
        if self.current_piece == 0:
            self.current_coord = BlocklesGame.STRAIGHT_PIECE[:] # this makes deep copies!
        elif self.current_piece == 1:
            self.current_coord = BlocklesGame.RIGHT_L_PIECE[:]
        elif self.current_piece == 2:
            self.current_coord = BlocklesGame.LEFT_L_PIECE[:]
        elif self.current_piece == 3:
            self.current_coord = BlocklesGame.T_PIECE[:]
        elif self.current_piece == 4:
            self.current_coord = BlocklesGame.SQUARE_PIECE[:]
        elif self.current_piece == 5: 
            self.current_coord = BlocklesGame.S_PIECE[:]
        elif self.current_piece == 6:
            self.current_coord = BlocklesGame.Z_PIECE[:]
  
    def update(self):
        self.generate_piece()
        for tetr in self.current_coord:
            x_coord = tetr[0]
            y_coord = tetr[1]
            self.board[x_coord][y_coord] = str(self.current_piece)









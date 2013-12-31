"""

This will contain the main game logic behind Blockles. The main class will query this class to figure out how to display the
current state of the game to the player.

"""

import random
import copy

class BlocklesGame:

    STRAIGHT_PIECE  = [ [0,5], [1,5], [2,5], [3,5] ]
    RIGHT_L_PIECE   = [ [0,5], [1,5], [2,5], [2,6] ]
    LEFT_L_PIECE    = [ [0,5], [1,5], [2,5], [2,4] ]
    T_PIECE         = [ [0,5], [1,4], [1,5], [1,6] ]
    SQUARE_PIECE    = [ [0,5], [0,6], [1,5], [1,6] ]
    S_PIECE         = [ [0,5], [1,5], [1,4], [0,6] ]
    Z_PIECE         = [ [0,5], [1,5], [0,4], [1,6] ]

    DOWN            = [1, 0]
    LEFT            = [0, -1]
    RIGHT           = [0,  1]
    BLANK           = 'A'

    def __init__(self):
        self.board = [['A' for y in range(10)] for x in range(20)]
        self.current_piece = -1
        self.current_coord = []
        self.speed = 500 # Higher is slower
        self.generate_piece()

    def generate_piece(self):
        self.current_piece = int(random.random()*7)
        if self.current_piece == 0:
            self.current_coord = copy.deepcopy(BlocklesGame.STRAIGHT_PIECE)
        elif self.current_piece == 1:
            self.current_coord = copy.deepcopy(BlocklesGame.RIGHT_L_PIECE)
        elif self.current_piece == 2:
            self.current_coord = copy.deepcopy(BlocklesGame.LEFT_L_PIECE)
        elif self.current_piece == 3:
            self.current_coord = copy.deepcopy(BlocklesGame.T_PIECE)
        elif self.current_piece == 4:
            self.current_coord = copy.deepcopy(BlocklesGame.SQUARE_PIECE)
        elif self.current_piece == 5: 
            self.current_coord = copy.deepcopy(BlocklesGame.S_PIECE)
        elif self.current_piece == 6:
            self.current_coord = copy.deepcopy(BlocklesGame.Z_PIECE)
  
    def update(self): 
        self.set_board(self.current_coord, self.current_piece)

    def move_piece(self, direction):
        old_coord = copy.deepcopy(self.current_coord)
        self.set_board(self.current_coord, BlocklesGame.BLANK)
        for elem in self.current_coord:
            elem[0] += direction[0]
            elem[1] += direction[1]
            if elem[1] < 0 or elem[1] >= 10:
                    self.current_coord = old_coord
                    return True
            if elem[0] >= 20 or self.board[elem[0]][elem[1]] != 'A':
                self.generate_piece()
                self.set_board(old_coord, self.current_piece)
                return False
        return True

    def jump_down(self):
        while True:
            if self.move_piece(BlocklesGame.DOWN) == False:
                break


    def set_board(self, piece, piece_id):
        for tetr in piece:
            x_coord = tetr[0]
            y_coord = tetr[1]
            self.board[x_coord][y_coord] = piece_id









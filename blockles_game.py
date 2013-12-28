"""

This will contain the main game logic behind Blockles. The main class will query this class to figure out how to display the
current state of the game to the player.

"""

import random

class BlocklesGame:

    def __init__(self):
        self.board = [['A' for y in range(10)] for x in range(20)]
        self.current_piece = -1
        self.current_coord = []
    

    def generate_piece(self):
        self.current_piece = int(random.random()*7)
        if self.current_piece == 0:
            self.current_coord.append( [0,0] )
        elif self.current_piece == 1:
            self.current_coord.append( [1,1] )
        elif self.current_piece == 2:
            self.current_coord.append( [2,2] )
        elif self.current_piece == 3:
            self.current_coord.append( [3,3] )
        elif self.current_piece == 4:
            self.current_coord.append( [4,1] )
        elif self.current_piece == 5: 
            self.current_coord.append( [5,1] )
        elif self.current_piece == 6:
            self.current_coord.append( [6,1] )
    
    def update(self):
        self.generate_piece()
        for tetr in self.current_coord:
            x_coord = tetr[0]
            y_coord = tetr[1]
            self.board[x_coord][y_coord] = self.current_piece


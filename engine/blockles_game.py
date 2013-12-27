"""

This will contain the main game logic behind Blockles. The main class will query this class to figure out how to display the
current state of the game to the player.

"""

class BlocklesGame:

    def __init__(self):
        self.board = []
        for i in range(20):
            self.board.append([])
            for j in range(10):
                self.board[i].append('A')

    

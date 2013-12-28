import pygame, sys
from pygame.locals import *

from blockles_game import *

# Initialize colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DOWN = [1, 0]

def terminate():
    pygame.quit()
    sys.exit()

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((200, 400))
    pygame.display.set_caption('Blockles rev 0.1')

    game = BlocklesGame()
    last_time = 0
    current_time = 0

    xpos = 10
    ypos = 10

    # Main game loop
    while True:
        DISPLAYSURF.fill(WHITE)

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate();

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate();
                elif event.key == K_RIGHT:                
                    xpos += 5
                elif event.key == K_LEFT:
                    xpos -= 5
                elif event.key == K_UP:
                    ypos -= 5
                elif event.key == K_DOWN:
                    ypos += 5
        
        current_time = pygame.time.get_ticks()
        if (current_time - last_time) >= game.speed:
            last_time = current_time
            game.move_piece(DOWN)
        game.update()        

        # Draw the board
        for y_coord in range(len(game.board)):
            for x_coord in range(len(game.board[y_coord])):
                if game.board[y_coord][x_coord] != 'A':
                    tile = pygame.Rect(x_coord*20, y_coord*20, 20, 20)       
                    pygame.draw.rect(DISPLAYSURF, BLUE, tile, 1)

        pygame.display.update()

if __name__ == '__main__':
    main()







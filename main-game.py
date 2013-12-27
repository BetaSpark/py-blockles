import pygame, sys
from pygame.locals import *

# Initialize colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def terminate():
    pygame.quit()
    sys.exit()

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Hello World!')
    img = pygame.image.load('giggle.png')

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
        
        pygame.draw.circle(DISPLAYSURF, BLUE, (xpos, ypos), 20, 0)

        pygame.display.update()

if __name__ == '__main__':
    main()







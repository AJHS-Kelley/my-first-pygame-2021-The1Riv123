# ny First pyGame, Jason Rivers, 11/30/21 1:15pm  v0.3

import pygame, sys
from pygame.locals import *

#initialize PyGame
pygame.init() 

# Setup the window to draw on.
windowSurface = pygame.display.set_mode ((500,400)), 0, 32)
pygame.display.set_caption ('my First PyGame')

#setup color values.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255) 
BROWN = (165, 42, 42)
# ny First pyGame, Jason Rivers, 11/30/21 1:25pm  v0.4

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

#Setup the fonts
basicFont = pygame.font.sysfont(None, 48)

#Setup the text
text = basicFont.render('Hello,world!,' True. WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery
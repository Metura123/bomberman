from utils import draw_pixels
from Stone import Stone
from Bomb import Bomb
import pygame
pygame.init()

run = True  # Game Loop
clock = pygame.time.Clock() # Game Clock

# Colors
GREEN = (0,150,0)
# End Colors

# Map
minimap = [
    [Stone()] * 33,
    [Stone(),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Stone()],
    [Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone()],
    [Stone(),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Stone()],
    [Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone()],
    [Stone(),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Stone()],
    [Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone()],
    [Stone(),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Stone()],
    [Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone()],
    [Stone(),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Stone()],
    [Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone()],
    [Stone(),0,0,0,0,0,0,0,0,0,0,0,0,Bomb(),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Stone()],
    [Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone()],
    [Stone(),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Stone()],
    [Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone()],
    [Stone(),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Stone()],
    [Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone()],
    [Stone(),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Stone()],
    [Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone()],
    [Stone(),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Stone()],
    [Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone()],
    [Stone(),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Stone()],
    [Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone(),0,Stone()],
    [Stone(),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Stone()],
    [Stone()] * 33,
]
# End Map

WIDTH, HEIGHT = 1056, 800           # Screen Resolution
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))       # Window Initialization
pygame.display.set_caption("Bomberman")

while run: 
    clock.tick(60) # Game FPS
    WINDOW.fill(GREEN)  # Draw window
    draw_pixels(WINDOW, minimap)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

pygame.quit()
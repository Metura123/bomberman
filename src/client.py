from utils import init_map, draw_pixels
from Entities.Stone import Stone
from Entities.Bomb import Bomb
from Entities.Player import Player
import pygame, threading, sys
pygame.init()

run = True  # Game Loop
clock = pygame.time.Clock() # Game Clock

# Colors
GREEN = (0,150,0)
# End Colors

# Map
minimap = []
obstacles = []
init_map(minimap,obstacles, "map.txt")
# End Map

WIDTH, HEIGHT = 1056, 800           # Screen Resolution
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))       # Window Initialization
pygame.display.set_caption("Bomberman")

player = Player(32, 32)

while run: 
    clock.tick(60) # Game FPS
    WINDOW.fill(GREEN)  # Draw window
    draw_pixels(WINDOW, minimap)
    player.move(obstacles)
    player.draw(WINDOW)
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
            break

pygame.quit()
from utils import draw_pixels
import pygame
pygame.init()

run = True  # Game Loop
clock = pygame.time.Clock() # Game Clock

# Colors
GREEN = (0,150,0)
# End Colors

WIDTH, HEIGHT = 1056, 800           # Screen Resolution
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))       # Window Initialization
pygame.display.set_caption("Bomberman")

while run: 
    clock.tick(60) # Game FPS
    WINDOW.fill(GREEN)  # Draw window
    draw_pixels(WINDOW, "map.txt")
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

pygame.quit()
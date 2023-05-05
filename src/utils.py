import pygame
# Images
STONE = pygame.image.load("img/stone-32.png")
BOMB = pygame.image.load("img/bomb-32-1.png")
BARREL = pygame.image.load("img/barrel-32.png")
# End Images

def draw_pixels(WINDOW,minimap):
    x = 0
    y = 0
    resolution = 32
    for row in minimap:
        for column in row:
            if column != 0:
                if column.id == 1:
                    WINDOW.blit(STONE,(x, y))
                if column.id == 2:
                    column.draw(WINDOW,x,y)
                if column.id == 3:
                    WINDOW.blit(BARREL, (x, y))

            x += resolution
        x = 0
        y += resolution


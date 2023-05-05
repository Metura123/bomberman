import pygame
# Images
STONE = pygame.image.load("img/stone-32_2.png")
BOMB = pygame.image.load("img/bomb-32.png")
# End Images

def draw_pixels(WINDOW,file_location):
    x = 0
    y = 0
    resolution = 32

    with open(file_location, "r") as file:
        for line in file:
            for id in line:
                if id == "1":
                    WINDOW.blit(STONE,(x, y))
                if id == "2":
                    WINDOW.blit(BOMB, (x, y))
                x += resolution
            
            x = 0
            y += resolution


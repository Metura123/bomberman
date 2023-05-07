from Entities.Stone import Stone
from Entities.Bomb import Bomb
import pygame
# Images
STONE = pygame.image.load("img/stone-32.png")
BOMB = pygame.image.load("img/bomb-32-1.png")
BARREL = pygame.image.load("img/barrel-32.png")
# End Images
# IDs
EMPTY = "0"
STONE_ID = "1"
BOMB_ID = "2"
# End IDs

def init_map(minimap,obstacles, map_file_location):
    x = 0
    y = 0
    map_list = []
    obstacles_list = []
    resolution = 32
    with open(map_file_location, "r") as file:
        for row,line in enumerate(file):
            to_append = [] # to create the objects such as stone(), bomb() and append to it then append to the main minimap 
            for column, value in enumerate(line):
                if value == EMPTY:
                    to_append.append(0)
                if value == STONE_ID:
                    stone = Stone(x, y, row, column)
                    try:
                        if stone.collision_area:
                            obstacles_list.append(stone.collision_area)
                    except:
                        pass
                    to_append.append(stone)
                if value == BOMB_ID:
                    to_append.append(Bomb(x, y, row, column))
                
                x += resolution
            
            map_list.append(to_append)
            x = 0
            y += resolution

        minimap[:] = map_list
        obstacles[:] = obstacles_list

def draw_pixels(WINDOW,minimap):
        for line in minimap:
            for entity in line:
                try:
                    entity.draw(WINDOW)
                except:
                    pass

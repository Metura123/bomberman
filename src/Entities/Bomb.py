import pygame
pygame.init()

class Bomb:
    id = 3
    def __init__(self,x,y,row,column):
        self.x = x
        self.y = y
        self.row = row
        self.column = column
        self.counter = 0

    def draw(self,WINDOW):
        frame_1 = pygame.image.load("img/bomb-32-1.png")
        frame_2 = pygame.image.load("img/bomb-32-2.png")
        if self.counter < 10:
            WINDOW.blit(frame_1, (self.x, self.y))
        elif  10 <= self.counter < 20:
            WINDOW.blit(frame_2, (self.x, self.y))

        if self.counter == 20:
            self.counter = 0
        else:
            self.counter += 1

    def explode_bomb(self,minimap,obstacles):
        try:
            if minimap[self.row - 1][self.column].id == 2:
                obstacles.remove(minimap[self.row - 1][self.column].collision_area)
                minimap[self.row - 1][self.column] = 0
        except:
            pass

        try:
            if minimap[self.row + 1][self.column].id == 2:
                obstacles.remove(minimap[self.row + 1][self.column].collision_area)
                minimap[self.row + 1][self.column] = 0
        except:
            pass

        try:
            if minimap[self.row][self.column + 1].id == 2:
                obstacles.remove(minimap[self.row][self.column + 1].collision_area)
                minimap[self.row][self.column + 1] = 0
        except:
            pass

        try:
            if minimap[self.row][self.column - 1].id == 2:
                obstacles.remove(minimap[self.row][self.column - 1].collision_area)
                minimap[self.row][self.column - 1] = 0
        except:
            pass

        minimap[self.row][self.column] = 0


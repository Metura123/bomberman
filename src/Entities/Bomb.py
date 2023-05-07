import pygame
pygame.init()

class Bomb:
    id = 2
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
        


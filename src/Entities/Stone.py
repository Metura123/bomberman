import pygame

class Stone:
    id = 1

    def __init__(self,x,y,row,column):
        self.x = x
        self.y = y
        self.row = row
        self.column = column
        self.image = pygame.image.load("img/stone-32.png")
        if not self.row == 0 and not self.column == 0 and not self.row == 24 and not self.column == 32: 
            self.collision_area = pygame.rect.Rect(self.x + 3, self.y + 3, 26, 26)

    def draw(self,WINDOW):
        WINDOW.blit(self.image, (self.x, self.y))
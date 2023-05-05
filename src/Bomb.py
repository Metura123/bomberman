import pygame
pygame.init()

class Bomb:
    id = 2
    def __init__(self):
        self.counter = 0
        self.frame_1 = pygame.image.load("img/bomb-32-1.png")
        self.frame_2 = pygame.image.load("img/bomb-32-2.png")

    def draw(self,WINDOW,x,y):
        if self.counter < 10:
            WINDOW.blit(self.frame_1, (x, y))
        elif  10 <= self.counter < 20:
            WINDOW.blit(self.frame_2, (x, y))

        if self.counter == 20:
            self.counter = 0
        else:
            self.counter += 1
        


import pygame
pygame.init()

class Player:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.velocity = 2
        self.image = pygame.image.load("img/barrel-32.png")
        self.collision_area = pygame.rect.Rect(self.x + 6, self.y + 6, 20, 20)

    def move(self,obstacles):
        keys = pygame.key.get_pressed()

        index = self.collision_area.collidelist(obstacles)
        if index != -1:
            entity = obstacles[index]
            if keys[pygame.K_w]:
                if entity.top <= self.collision_area.bottom <= entity.bottom:
                    self.y -= self.velocity
            if keys[pygame.K_a]:
                if entity.left <= self.collision_area.right <= entity.right:
                    self.x -= self.velocity
            if keys[pygame.K_s]:
                if entity.top <= self.collision_area.top <= entity.bottom:
                    self.y += self.velocity
            if keys[pygame.K_d]: 
                if entity.left <= self.collision_area.left <= entity.right:
                    self.x += self.velocity

        else:
            if keys[pygame.K_w]:
                if self.collision_area.top - self.velocity > 26:
                    self.y -= self.velocity
            if keys[pygame.K_a]:
                if self.collision_area.left - self.velocity > 26:
                    self.x -= self.velocity
            if keys[pygame.K_s]:
                if self.collision_area.bottom + self.velocity < 800 - 26:
                    self.y += self.velocity
            if keys[pygame.K_d]: 
                if self.collision_area.right + self.velocity < 1056 - 26:
                    self.x += self.velocity

        self.collision_area = pygame.rect.Rect(self.x + 6, self.y + 6, 20, 20)

    def draw(self,WINDOW):
        WINDOW.blit(self.image, (self.x, self.y))
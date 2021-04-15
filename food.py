import pygame

class food:
    #X, Y, def destroy, def get
    radius = 3
    def __init__(self, x, y):
        """Setting up the new instance"""
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, (200,150,100), (self.x,self.y), self.radius)

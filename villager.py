import pygame
import random

class villager:
    # X, Y, velx, vely, accx, accy,
    radius = 8
    velX = 0
    velY = 0
    accX = 0
    accY = 0
    maxSpd = 2

    def __init__(self, x, y):
        """Setting up the new instance"""
        self.x = x
        self.y = y

    #movement

    #replication

    #Draw
    def draw(self, screen):
        pygame.draw.circle(screen, (250,0,0), (self.x,self.y), self.radius)

    #check all food and see if touching

    #check all villagers and see if touching

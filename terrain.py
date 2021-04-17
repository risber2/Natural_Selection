from perlin_noise import PerlinNoise
import pygame
import math

class terrain:
    blocks = [] #2D array with 1 as land and 0 as water
    landCutoff = 0.05
    noiseSeed = 5
    noiseOctaves = 4
    zoom = 100
    noiseX = 40
    noiseY = 1
    def __init__(self, width, height, size):
        #Setting up the new instance
        self.width = width
        self.height = height
        self.size = size #number of blocks per row/column

    def setup(self):
        #create the block terrain using perlin noise
        noise = PerlinNoise(octaves=self.noiseOctaves, seed=self.noiseSeed)

        self.blocks =[[0 for j in range(self.size)] for i in range(self.size)]

        for i in range(self.size):
            for j in range(self.size):
                value = noise([(i+self.noiseX)/self.zoom, (j+self.noiseY)/self.zoom])
                if value <= self.landCutoff: #water
                    self.blocks[i][j] = 0
                else:
                    self.blocks[i][j] = 1

    def draw(self, screen):
        xlength = self.width/self.size
        ylength = self.height/self.size

        for x in range(len(self.blocks)):
            for y in range(len(self.blocks[0])):
                rect = pygame.Rect(x*xlength,y*ylength,xlength,ylength)
                if(self.blocks[x][y] == 0): #water
                    pygame.draw.rect(screen,pygame.Color(0,0,255),rect) #blue
                else: #1 = land
                    pygame.draw.rect(screen,pygame.Color(0,255,0),rect) #green

    def getBlock(self,x,y):
        '''
        arg: x and y coordinates of terrain
        description: will give the type of block at x and y
        return: 0 for water and 1 for land
        '''
        #will be error if x/y are beyond the screen
        return(self.blocks[math.floor(x/self.width*self.size)][math.floor(y/self.width*self.size)])

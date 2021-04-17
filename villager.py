import pygame
import random
import customMath
from customMath import vector
from food import food
from terrain import terrain

class villager:
    #variables
    radius = 8
    health = 100
    velX, velY, accX, accY= 0, 0, 0, 0

    #DNA
    DNA = {
        "maxSpeed" : random.randrange(5)+0.1,
        "foodAttraction" : random.randrange(-5,5),
        "mateAttraction" : random.randrange(-5,5),
        "waterAttraction" : random.randrange(-5,5),
        "sightDistance" : random.randrange(20)

    }

    def __init__(self, x, y):
        """Setting up the new instance"""
        self.x = x
        self.y = y
    #movement

    #replication

    #Draw
    def draw(self, screen):
        pygame.draw.circle(screen, (250,0,0), (self.x,self.y), self.radius)

    #Update
    def update(self, terra, foodList, villagerList):
        #reduce health
        self.health -= self.DNA["maxSpeed"]/50
        v1 = self.foodVector(foodList)
        v2 = self.villagerVector(villagerList)
        v3 = self.terrainVector(terra)
        finalVector = self.totalVectors(v1, v2, v3)
        print(finalVector.x, finalVector.y)
    #foodVector
    def foodVector(self, foodList):
        vectors = []
        for item in foodList:
            if customMath.distance(item.x, item.y, self.x, self.y) <= self.DNA["sightDistance"]: #if visable
                foodDesire = vector(item.x-self.x, item.y-self.y)
                foodDesire.setMagnitude(self.DNA["foodAttraction"])
                vectors.append(foodDesire)
        return vectors
    #VillagerVector
    def villagerVector(self, villagerList):
        vectors = []
        for item in villagerList:
            if customMath.distance(item.x, item.y, self.x, self.y) <= self.DNA["sightDistance"]: #if visable
                mateDesire = vector(item.x-self.x, item.y-self.y)
                mateDesire.setMagnitude(self.DNA["mateAttraction"])
                vectors.append(mateDesire)
        return vectors
    #terrainVector
    def terrainVector(self, terra):
        vectors = []

        bWidth = terra.width / terra.size #width of each block
        bHeight = terra.height / terra.size #height of each block

        checkingVectors = (
        vector(self.x+bWidth, self.y), #right
        vector(self.x-bWidth, self.y), #left
        vector(self.x, self.y-bHeight), #top
        vector(self.x+bWidth, self.y+bHeight), #bottom
        vector(self.x+bWidth, self.y-bHeight), #topRight
        vector(self.x-bWidth, self.y-bHeight), #topLeft
        vector(self.x-bWidth, self.y+bHeight), #bottomLeft
        vector(self.x+bWidth, self.y+bHeight) #bottomRight
        );
        for location in checkingVectors:
            if terra.getBlock(location.x, location.y) == 0:  #right
                waterDesire = location
                waterDesire.setMagnitude(self.DNA["waterAttraction"])
                vectors.append(waterDesire)
        return vectors
    #Calculate total vector
    def totalVectors(self, list1, list2, list3):
        total = vector(0,0)
        for vec in list1:
            total = vec + total
        for vec in list2:
            total = vec + total
        for vec in list3:
            total = vec + total
        total.setMagnitude(self.DNA["maxSpeed"])
        return total
    #pass total vector into movement function

    #call replication function

    #check all food and see if touching
    def checkFood(foodList):
        pass
    #check all villagers and see if touching
    def checkVillagers(villagerList):
        pass
    def checkTerrain(terra):
        pass

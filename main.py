import pygame
import random
from villager import villager
from food import food
from terrain import terrain

def setup(width, height):
	'''
	arg: width and height of soon to be screen
	description: setup the screen and init window
	return: screen object
	'''
	#print our names
	print("Ryan Isber")
	print("Jordan Dickman")
	print("Daniel Lusdyk")

	#initialize pygame
	pygame.init()

	#create screen
	screen = pygame.display.set_mode((width,height))

	#set title
	pygame.display.set_caption("Natural Selection Simulation")

	return screen

def spawnFood(terra, numberOfFood):
	"""
	arg: the terrain (terra) to spawn the food onto, the number of food to spawn
	description: spawns food and stors it into a foodList
	return: list containing all food objects that were instantiated
	"""
	foodList = []
	for i in range(numberOfFood):
		while True:
			x = random.randrange(terra.width)
			y = random.randrange(terra.height)
			if(terra.getBlock(x,y) > 0): #if land
				foodList.append(food(x,y))
				break
	return foodList

def spawnVillagers(terra, numberOfVillagers):
		"""
		arg: the terrain (terra) to spawn the food onto, the number of food to spawn
		description: spawns food and stors it into a foodList
		return: list containing all food objects that were instantiated
		"""
		villagerList = []
		for i in range(numberOfVillagers):
			while True:
				x = random.randrange(terra.width)
				y = random.randrange(terra.height)
				if(terra.getBlock(x,y) > 0): #if land
					villagerList.append(villager(x,y))
					break
		return villagerList


def main():
	#set variables
	width = 600
	height = 600
	size = 50

	foodNum = 1
	villagerNum = 1
	foodList = []
	villagerList = []

	#create screen and setup environment
	simScreen = setup(width,height)

	#create terrain
	terra = terrain(width, height, size)
	terra.setup()
	#spawn food
	foodList = spawnFood(terra, foodNum)
	#spawn villagers
	villagerList = spawnVillagers(terra, villagerNum)
	print(len(villagerList))
	#main game loop
	running = True
	while running:
		for event in pygame.event.get():
			#if quitting
			if event.type == pygame.QUIT:
				running = False
		#=========================== MAIN GAME LOOP ===========================#
		# Draw Terrain
		terra.draw(simScreen)
		# Draw food
		for edible in foodList:
			edible.draw(simScreen)
		# Draw villagers
		for person in villagerList:
			person.update(terra, foodList, villagerList)
			person.draw(simScreen)
		#=======================================================================#
		#Update screen
		pygame.display.update()
main()

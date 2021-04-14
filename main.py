import pygame

def main():
	#print our names
	print("Ryan Isber")
	print("Jordan Dickman")
	print("Daniel Lusdyk")

	#initialize pygame
	pygame.init()

	#create screen
	screen = pygame.display.set_mode((800,600))
	
	#set title
	pygame.display.set_caption("Natural Selection Simulation")

	#main game loop
	running = True
	while running:
		for event in pygame.event.get():
			#if quitting
			if event.type == pygame.QUIT:
				running = False
		
main()

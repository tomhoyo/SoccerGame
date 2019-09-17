import pygame

continuer = True

pygame.init()
ecran = pygame.display.set_mode((300, 200))

while continuer:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			continuer = False


pygame.quit()
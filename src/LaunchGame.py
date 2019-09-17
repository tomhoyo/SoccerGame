import pygame

continuer = True

pygame.init()
ecran = pygame.display.set_mode((1000, 700))
icon = pygame.image.load("ressources/Soccer_Ball_icon.png")

pygame.display.set_caption("SoccerGame")
pygame.display.set_icon(icon)

imgHand = pygame.image.load("ressources/stickeroid_5bf543f41865d.png")
ecran.blit(imgHand, (0, 0))

while continuer:
	
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			continuer = False

	pygame.display.flip()


pygame.quit()
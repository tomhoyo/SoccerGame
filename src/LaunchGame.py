import pygame

continuer = True

width = 1000
height = 700

x = 50
y = 200

limX = width
limY = height 

speed = 20

pygame.init()
ecran = pygame.display.set_mode((width, height))
icon = pygame.image.load("ressources/Soccer_Ball_icon.png")

pygame.display.set_caption("SoccerGame")
pygame.display.set_icon(icon)

imgHand = pygame.image.load("ressources/stickeroid_5bf543f41865d.png")

pygame.draw.rect(ecran, (255, 255, 255), (0, 0, 1000, 700))
ecran.blit(imgHand, (x, y))
while continuer:
	
	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:
			print(str(x) + " - " + str(y))

			if event.key == pygame.K_f:
				continuer = False

			if event.key == pygame.K_w and y > 0:
				y-=speed 
			if event.key == pygame.K_s and y < limY:
				y+=speed 
			if event.key == pygame.K_a and x > 0:
				x-=speed
			if event.key == pygame.K_d and x < limY:
				x+=speed

			pygame.draw.rect(ecran, (255, 255, 255), (0, 0, width, height))
			ecran.blit(imgHand, (x, y))

	pygame.display.flip()

pygame.quit()
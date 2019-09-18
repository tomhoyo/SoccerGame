import pygame
import time

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

imgHand = pygame.image.load("ressources/Sanstitre.png")

pygame.draw.rect(ecran, (255, 255, 255), (0, 0, width, height))
ecran.blit(imgHand, (x, y))

while continuer:
	
	for event in pygame.event.get():
		keystate = pygame.key.get_pressed()

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_f:
				continuer = False

			if (event.key == pygame.K_w or keystate[pygame.K_w]) and y > 0:
				y-=speed 
				#time.sleep(0.5)

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
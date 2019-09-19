import pygame
import time
import Player

continuer = True

width = 1000
height = 600

speed = 1

pygame.init()
player1 = Player(50, 200)
ecran = pygame.display.set_mode((width, height))
icon = pygame.image.load("ressources/Soccer_Ball_icon.png")
print(type(icon))
pygame.display.set_caption("SoccerGame")
pygame.display.set_icon(icon)


pygame.draw.rect(ecran, (255, 255, 255), (0, 0, width, height))
ecran.blit(player1.imgPlayer, (player1.getX(), player1.getY()))

limX = width - player1.getImgPlayer().get_width()
limY = height - player1.getImgPlayer().get_height()

z = q = s = d =0
"""
while continuer:
	keystate = pygame.key.get_pressed()
	if keystate[pygame.K_w] and player1.getY() > 0:
		player1.setY(player1.getY()-speed)
	if keystate[pygame.K_s] and player1.getY() < limY:
		player1.setY(player1.getY()+speed)
	if keystate[pygame.K_a] and player1.getX() > 0:
		player1.setX(player1.getX()-speed)
	if keystate[pygame.K_d] and player1.getX() < limX:
		player1.setX(player1.getX()+speed)

	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_f:
				continuer = False

	pygame.draw.rect(ecran, (255, 255, 255), (0, 0, width, height))
	ecran.blit(player1.getImgPlayer(), (player1.getX(), player1.getY()))

	pygame.display.flip()
"""
pygame.quit()
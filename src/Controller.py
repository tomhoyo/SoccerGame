import pygame
from Player import *


class Controller:

	pygame.init()
	continuer = True
	width = 1000
	height = 600
	players = []
	ecran = pygame.display.set_mode((width, height))

	def __init__(self):
		self.continuer = True

		self.players.append(Player(self, 50, 200))

		icon = pygame.image.load("ressources/Soccer_Ball_icon.png")

		pygame.display.set_caption("SoccerGame")
		pygame.display.set_icon(icon)

		pygame.draw.rect(self.ecran, (255, 255, 255), (0, 0, self.width, self.height))
		self.ecran.blit(self.players[0].imgPlayer, (self.players[0].getX(), self.players[0].getY()))

	def startGame(self):
		while self.continuer:
			keystate = pygame.key.get_pressed()
			if keystate[pygame.K_w] and self.players[0].getY() > 0:
				self.players[0].moveUp()
			if keystate[pygame.K_s] and self.players[0].getY() < self.players[0].limY:
				self.players[0].moveDown()
			if keystate[pygame.K_a] and self.players[0].getX() > 0:
				self.players[0].moveLeft()
			if keystate[pygame.K_d] and self.players[0].getX() < self.players[0].limX:
				self.players[0].moveRight()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_f:
						self.continuer = False

			pygame.draw.rect(self.ecran, (255, 255, 255), (0, 0, self.width, self.height))
			self.ecran.blit(self.players[0].getImgPlayer(), (self.players[0].getX(), self.players[0].getY()))

			pygame.display.flip()
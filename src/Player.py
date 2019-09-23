import pygame

class Player():

	x = 0
	y = 0
	imgPlayer = pygame.image.load("ressources/Sanstitre.png")

	def getX(self):
		return self.x

	def setX(self, x):
		self.x = x

	def getY(self):
		return self.y

	def setY(self, y):
		self.y = y

	def getImgPlayer(self):
		return self.imgPlayer



import pygame

class Ball:

	x = 0
	y = 0
	imgPlayer = pygame.image.load("ressources/player2.png")
	speed = 0.5
	dirX = 0
	dirY = 0

	def __init__(self, x, y):
		self.x = x
		self.y = y

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

	def getSpeed(self):
		return self.speed

	def setSpeed(self, speed):
		self.speed = speed
"""
	def moveUp(self):
		self.setY(self.getY()-self.getSpeed())

	def moveDown(self):
		self.setY(self.getY()+self.getSpeed())

	def moveRight(self):
		self.setX(self.getX()+self.getSpeed())

	def moveLeft(self):
		self.setX(self.getX()-self.getSpeed())
"""
	#def calculDirX():
	#def calculDirY():	
import pygame

class Player:

	x = 0
	y = 0
	imgPlayer = pygame.image.load("ressources/player2.png")
	speed = 0.5

	limY = 0
	limX = 0

	def __init__(self, ctrl, x, y):
		self.x = x
		self.y = y

		self.limX = ctrl.width - self.getImgPlayer().get_width()
		self.limY = ctrl.height - self.getImgPlayer().get_height()

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

	def setlimY(self, limY):
		self.limY = limY

	def getlimY(self):
		return self.limY

	def setlimX(self, limX):
		self.limX = limX

	def getlimY(self):
		return self.limX

	def setSpeed(self, speed):
		self.speed = speed

	def moveUp(self):
		self.setY(self.getY()-self.getSpeed())

	def moveDown(self):
		self.setY(self.getY()+self.getSpeed())

	def moveRight(self):
		self.setX(self.getX()+self.getSpeed())

	def moveLeft(self):
		self.setX(self.getX()-self.getSpeed())

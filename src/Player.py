import pygame

class Player:

	x = 0
	y = 0
	imgSkin = pygame.image.load("ressources/player3.png")
	speed = 0

	limY = 0
	limX = 0

	def __init__(self, ctrl, x, y):
		self.speed = (ctrl.frame.width * 1.5) / 1366

		self.imgSkin = pygame.transform.scale(self.imgSkin, (int(ctrl.frame.width * 0.04), int(ctrl.frame.height * 0.13)))

		self.x = x - self.getImgSkin().get_width()/2
		self.y = y - self.getImgSkin().get_height()/2

		self.limX = ctrl.frame.width - self.getImgSkin().get_width()
		self.limY = ctrl.frame.height - self.getImgSkin().get_height()

	def getX(self):
		return self.x

	def setX(self, x):
		self.x = x

	def getY(self):
		return self.y

	def setY(self, y):
		self.y = y

	def getImgSkin(self):
		return self.imgSkin

	def getSpeed(self):
		return self.speed

	def setSpeed(self, speed):
		self.speed = speed

	def setlimY(self, limY):
		self.limY = limY

	def getlimY(self):
		return self.limY

	def setlimX(self, limX):
		self.limX = limX

	def getlimY(self):
		return self.limX

	def moveUp(self):
		self.setY(self.getY()-self.getSpeed())
		
	def moveDown(self):
		self.setY(self.getY()+self.getSpeed())

	def moveRight(self):
		self.setX(self.getX()+self.getSpeed())

	def moveLeft(self):
		self.setX(self.getX()-self.getSpeed())

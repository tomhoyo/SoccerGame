import pygame
import math

class Ball:

	x = 0
	y = 0
	dirX = 0
	dirY = 0
	speed = 0
	unspeed = 0
	maxSpeed = 2
	alpha = 0
	limY = 0
	limX = 0
	imgSkin = pygame.image.load("ressources/Soccer_Ball_icon.png")
	imgSkin = pygame.transform.scale(imgSkin, (50, 50))


	def __init__(self, ctrl, x, y):
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

	def getLimX(self):
		return self.limX

	def setLimX(self, limX):
		self.limX = limX

	def getLimY(self):
		return self.limY

	def setLimY(self, limY):
		self.limY = limY

	def getDirX(self):
		return self.dirX

	def setDirX(self, dirX):
		self.dirX = dirX

	def getDirY(self):
		return self.dirY

	def setDirY(self, dirY):
		self.dirY = dirY

	def getImgSkin(self):
		return self.imgSkin

	def getSpeed(self):
		return self.speed

	def setSpeed(self, speed):
		self.speed = speed

	def getMaxSpeed(self):
		return self.maxSpeed
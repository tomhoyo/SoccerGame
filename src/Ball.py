import pygame
import math

class Ball:

	x = 0
	y = 0
	dirX = 0
	dirY = 0
	speed = 0
	unspeed = 0
	limY = 0
	limX = 0
	alpha = 0
	v=0
	imgBall = pygame.image.load("ressources/Soccer_Ball_icon.png")
	imgBall = pygame.transform.scale(imgBall, (50, 50))



	def __init__(self, ctrl, x, y):
		self.x = x - self.getImgBall().get_width()/2
		self.y = y - self.getImgBall().get_height()/2

		self.limX = ctrl.width - self.getImgBall().get_width()
		self.limY = ctrl.height - self.getImgBall().get_height()


	def getX(self):
		return self.x

	def setX(self, x):
		self.x = x

	def getY(self):
		return self.y

	def setY(self, y):
		self.y = y

	def getImgBall(self):
		return self.imgBall

	def getSpeed(self):
		return self.speed

	def setSpeed(self, speed):
		self.speed = speed

	def hurtPlayer(self, xPlayer, yPlayer):
		self.alpha = math.atan2((self.y + self.getImgBall().get_height()/2 - yPlayer), (self.x + self.getImgBall().get_width()/2 - xPlayer))
		self.dirX = math.cos(self.alpha)
		self.dirY = math.sin(self.alpha)
		self.speed = 2
		self.unspeed = 0

	def hurtWallX(self):
		self.dirX *= -1

	def hurtWallY(self):
		self.dirY *= -1

	#def moveBall()
	def decelerate(self):
		if self.speed > 0:
			self.speed = -math.pow(self.unspeed, 2) + 2
			self.unspeed += 0.0005
		else:
			self.speed = 0


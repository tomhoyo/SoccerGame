import pygame

class Ball:

	x = 0
	y = 0
	imgBall = pygame.image.load("ressources/Soccer_Ball_icon.png")
	speed = 0.5
	dirX = 0
	dirY = 0

	def __init__(self, x, y):
		self.x = x - self.getImgBall().get_width()/2
		self.y = y - self.getImgBall().get_height()/2

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
from Ball import *


class BallController(object):

	nbrBall = 0
	ballsList = []

	def __init__(self, nbrBall):
		self.nbrBall = nbrBall

	def Createballs(self, ctrl):
		self.ballsList.append(Ball(ctrl, ctrl.width/2, ctrl.height/2))
		self.ballsList.append(Ball(ctrl, ctrl.width/2, ctrl.height/2 + 70))
		self.ballsList.append(Ball(ctrl, ctrl.width/2, ctrl.height/2 + 120))
		self.ballsList.append(Ball(ctrl, ctrl.width/2, ctrl.height/2 - 70))
		self.ballsList.append(Ball(ctrl, ctrl.width/2, ctrl.height/2 - 120))

	def collisionMovingObject(self, ball, xObject, yObject):
		ball.alpha = math.atan2((ball.y + ball.getImgBall().get_height()/2 - yObject), (ball.x + ball.getImgBall().get_width()/2 - xObject))
		ball.dirX = math.cos(ball.alpha)
		ball.dirY = math.sin(ball.alpha)
		ball.speed = 2
		ball.unspeed = 0

	def collisionWall(self, ball, ctrl):
		if ball.getX() <= 0 or ball.getX() >= ball.getLimX():
			ball.setDirX(ball.getDirX() * -1)
			if ball.getX() >= ball.getLimX():
				ctrl.scoreLeft += 1
			else:
				ctrl.scoreRight += 1
		if ball.getY() <= 0 or ball.getY() >= ball.getLimY():
			ball.setDirY(ball.getDirY() * -1)

	def decelerate(self, ball):
		if ball.speed > 0:
			ball.speed = -math.pow(ball.unspeed, 2) + 2
			ball.unspeed += 0.0005
		else:
			ball.speed = 0

	def move(self, ball):
		ball.setX(ball.getX() + ball.getSpeed() * ball.getDirX())
		ball.setY(ball.getY() + ball.getSpeed() * ball.getDirY())

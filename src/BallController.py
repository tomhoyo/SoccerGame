from Ball import *


class BallController(object):

	nbrBall = 0
	list = []

	def __init__(self, nbrBall):
		self.nbrBall = nbrBall

	def Createballs(self, ctrl):
		if self.nbrBall >= 1:
			self.list.append(Ball(ctrl, ctrl.frame.width/2, ctrl.frame.height/2))
		if self.nbrBall >= 2:
			self.list.append(Ball(ctrl, ctrl.frame.width/2, ctrl.frame.height/2 + 70))
		if self.nbrBall >= 3:
			self.list.append(Ball(ctrl, ctrl.frame.width/2, ctrl.frame.height/2 + 120))
		if self.nbrBall >= 4:
			self.list.append(Ball(ctrl, ctrl.frame.width/2, ctrl.frame.height/2 - 70))
		if self.nbrBall >= 5:
			self.list.append(Ball(ctrl, ctrl.frame.width/2, ctrl.frame.height/2 - 120))

	def checkCollisionMovingObject(self, ball, Object):
		ball.alpha = math.atan2((ball.y + ball.getImgSkin().get_height()/2 - (Object.getY() + Object.getImgSkin().get_height()/2)), (ball.x + ball.getImgSkin().get_width()/2 - (Object.getX() + Object.getImgSkin().get_width()/2)))
		ball.dirX = math.cos(ball.alpha)
		ball.dirY = math.sin(ball.alpha)

	def checkCollisionWall(self, ball, ctrl):
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
			ball.speed = -math.pow(ball.unspeed, 2) + ball.getMaxSpeed()
			ball.unspeed += 0.0003
		else:
			ball.speed = 0

	def move(self, ball):
		ball.setX(ball.getX() + ball.getSpeed() * ball.getDirX())
		ball.setY(ball.getY() + ball.getSpeed() * ball.getDirY())

	def calculSpeedAfterCollision(self, ball, Object, collisionPlayer):
		if collisionPlayer:
			ball.speed = ball.getMaxSpeed()
			ball.unspeed = 0
		else:
			ball.speed = (ball.getSpeed() + Object.getSpeed()) / 2
			Object.unspeed = ball.unspeed = math.sqrt(-ball.getSpeed() + ball.getMaxSpeed())


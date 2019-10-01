from Ball import *


class BallController(object):

	nbrBall = 0
	ballsList = []

	def __init__(self, nbrBall):
		self.nbrBall = nbrBall

	def Createballs(self, ctrl):
		self.ballsList.append(Ball(ctrl, ctrl.width/2, ctrl.height/2))
		self.ballsList.append(Ball(ctrl, ctrl.width/2, ctrl.height/2 + 70))
		#self.ballsList.append(Ball(ctrl, ctrl.width/2, ctrl.height/2 + 120))
		self.ballsList.append(Ball(ctrl, ctrl.width/2, ctrl.height/2 - 70))
		#self.ballsList.append(Ball(ctrl, ctrl.width/2, ctrl.height/2 - 120))


	def collisionMovingObject(self, ball, Object):
		ball.alpha = math.atan2((ball.y + ball.getImgSkin().get_height()/2 - (Object.getY() + Object.getImgSkin().get_height()/2)), (ball.x + ball.getImgSkin().get_width()/2 - (Object.getX() + Object.getImgSkin().get_width()/2)))
		ball.dirX = math.cos(ball.alpha)
		ball.dirY = math.sin(ball.alpha)

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
			ball.unspeed = math.sqrt(-ball.getSpeed() + ball.getMaxSpeed())

from Ball import *


class BallController(object):

	nbrBall = 0
	listObject = []
	listPos = []


	def __init__(self):
		pass

	def Createballs(self, ctrl, nbrBall):
		self.nbrBall = nbrBall

		self.CreatePos(ctrl)

		x = 0
		while x < self.nbrBall:
			self.listObject.append(Ball(ctrl, self.listPos[x][0], self.listPos[x][1]))
			x+=1

	def CreatePos(self, ctrl):
		self.listPos.append([ctrl.frame.width/2, ctrl.frame.height/2])
		x = 1
		while x < 3:
			self.listPos.append([ctrl.frame.width/2, ctrl.frame.height/2 + (int(ctrl.frame.height * 0.07) + int(ctrl.frame.height * 0.026)) * x])
			self.listPos.append([ctrl.frame.width/2, ctrl.frame.height/2 - (int(ctrl.frame.height * 0.07) + int(ctrl.frame.height * 0.026)) * x])
			x+=1

	def checkCollisionMovingObject(self, ball, Object):
		ball.alpha = math.atan2((ball.y + ball.getImgSkin().get_height()/2 - (Object.getY() + Object.getImgSkin().get_height()/2)), (ball.x + ball.getImgSkin().get_width()/2 - (Object.getX() + Object.getImgSkin().get_width()/2)))
		ball.dirX = math.cos(ball.alpha)
		ball.dirY = math.sin(ball.alpha)

	def checkCollisionWall(self, ball, ctrl):
		if ball.getX() <= 0 or ball.getX() >= ball.getLimX():
			ball.setDirX(ball.getDirX() * -1)
			if ball.getX() >= ball.getLimX():
				ctrl.scoreLeft += 1
				if ctrl.scoreLeft >= ctrl.scoreMax:
					ctrl.congratulateWinner("Left")
			else:
				ctrl.scoreRight += 1
				if ctrl.scoreRight >= ctrl.scoreMax:
					ctrl.congratulateWinner("Right")
			ctrl.restartGameAfterBut()
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

	def respawnBalls(self):
		x = 0
		for ball in self.listObject:
			ball.setSpeed(0)
			ball.setX(self.listPos[x][0] - ball.getImgSkin().get_width()/2)
			ball.setY(self.listPos[x][1] - ball.getImgSkin().get_height()/2)
			x+=1
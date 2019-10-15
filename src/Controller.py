from pygame import *
from PlayerController import *
from BallController import *
from Frame import *


class Controller:

	frame = Frame()
	players = PlayerController(2)
	balls = BallController(1)


	continuer = True
	scoreRight = 0
	scoreLeft = 0

	def __init__(self):
		self.continuer = True

		self.players.CreatePlayers(self)
		self.balls.Createballs(self)

	def startGame(self):
		while self.continuer:
			keystate = pygame.key.get_pressed()
			self.players.CheckKeyEventPLayers(keystate)
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_f or event.type == pygame.QUIT:
						pygame.quit() 
						quit()

			for ball in self.balls.listObject:
				for player in self.players.listObject:
					if ball.getX() > player.getX() and ball.getX() < player.getX() + player.getImgSkin().get_width() and ball.getY() > player.getY() and ball.getY() < player.getY() + player.getImgSkin().get_height() or ball.getX() + ball.getImgSkin().get_width() > player.getX() and ball.getX() + ball.getImgSkin().get_width() < player.getX() + player.getImgSkin().get_width() and ball.getY() > player.getY() and ball.getY() < player.getY() + player.getImgSkin().get_height() or ball.getX() + ball.getImgSkin().get_width() > player.getX() and ball.getX() + ball.getImgSkin().get_width() < player.getX() + player.getImgSkin().get_width() and ball.getY() + ball.getImgSkin().get_height() > player.getY() and ball.getY() + ball.getImgSkin().get_height() < player.getY() + player.getImgSkin().get_height() or ball.getX() > player.getX() and ball.getX() < player.getX() + player.getImgSkin().get_width() and ball.getY() + ball.getImgSkin().get_height() > player.getY() and ball.getY() + ball.getImgSkin().get_height() < player.getY() + player.getImgSkin().get_height():
						self.balls.checkCollisionMovingObject(ball, player)
						self.balls.calculSpeedAfterCollision(ball, player, True)
				for otherBall in self.balls.listObject:
					if (ball.getX() > otherBall.getX() and ball.getX() < otherBall.getX() + otherBall.getImgSkin().get_width() and ball.getY() > otherBall.getY() and ball.getY() < otherBall.getY() + otherBall.getImgSkin().get_height() or ball.getX() + ball.getImgSkin().get_width() > otherBall.getX() and ball.getX() + ball.getImgSkin().get_width() < otherBall.getX() + otherBall.getImgSkin().get_width() and ball.getY() > otherBall.getY() and ball.getY() < otherBall.getY() + otherBall.getImgSkin().get_height() or ball.getX() + ball.getImgSkin().get_width() > otherBall.getX() and ball.getX() + ball.getImgSkin().get_width() < otherBall.getX() + otherBall.getImgSkin().get_width() and ball.getY() + ball.getImgSkin().get_height() > otherBall.getY() and ball.getY() + ball.getImgSkin().get_height() < otherBall.getY() + otherBall.getImgSkin().get_height() or ball.getX() > otherBall.getX() and ball.getX() < otherBall.getX() + otherBall.getImgSkin().get_width() and ball.getY() + ball.getImgSkin().get_height() > otherBall.getY() and ball.getY() + ball.getImgSkin().get_height() < otherBall.getY() + otherBall.getImgSkin().get_height()) and (ball.getX != otherBall.getX and ball.getX != otherBall.getX):
						self.balls.checkCollisionMovingObject(ball, otherBall)
						self.balls.calculSpeedAfterCollision(ball, player, False)
				self.balls.checkCollisionWall(ball, self)
			
			for ball in self.balls.listObject:
				self.balls.decelerate(ball)
				self.balls.move(ball)

			self.balls.decelerate(ball)
			self.balls.checkCollisionWall(ball, self)
			self.balls.move(ball)

			self.frame.refreshFrame(self.balls, self.players, self.scoreLeft, self.scoreRight)

			
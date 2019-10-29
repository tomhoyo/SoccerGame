from pygame import *
from PlayerController import *
from BallController import *
from Frame import *


class Controller:

	frame = Frame()
	players = PlayerController()
	balls = BallController()

	stayInGame = True
	stayForm = True
	scoreRight = 0
	scoreLeft = 0
	scoreMax = 2

	def __init__(self):
		self.stayInGame = True

		self.formManager()

	def startGame(self):
		self.stayInGame = True
		winner = "0"
		while self.stayInGame:
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

				winner = self.balls.checkCollisionWall(ball, self)

				if winner != "0":
					self.stayInGame = False
					self.frame.gamePanel.displayWinner(self, winner)
					pygame.event.wait()
					break

			if self.stayInGame:
				for ball in self.balls.listObject:
					self.balls.decelerate(ball)
					self.balls.move(ball)

				self.frame.gamePanel.refreshGameFrame(self.balls, self.players, self.scoreLeft, self.scoreRight)

	def restartGameAfterBut(self):
		self.balls.respawnBalls()
		self.players.respawnPlayers()
		self.startGame()

	def initGame(self):
		self.players.listObject.clear()
		self.balls.listObject.clear()
		self.scoreRight = 0
		self.scoreLeft = 0
		self.players.CreatePlayers(self, 2)
		self.balls.Createballs(self, 1)

	def formManager(self):
		self.frame.formPanel.displayForm()
		self.stayForm = True

		while self.stayForm:
			self.initGame()
			self.startGame()

			"""
			check click button
			"""
from pygame import *
from PlayerController import *
from BallController import *
from Frame import *


class Controller:

	frame = Frame()
	players = PlayerController()
	balls = BallController()

	stayInGame = True
	stayInForm = True
	stayInApp = True
	scoreRight = 0
	scoreLeft = 0
	scoreMax = 10

	def __init__(self):
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

	def initGame(self, nbrPlayer, nbrBall):
		self.players.listObject.clear()
		self.balls.listObject.clear()
		self.scoreRight = 0
		self.scoreLeft = 0
		self.players.CreatePlayers(self, nbrPlayer)
		self.balls.Createballs(self, nbrBall)

	def formManager(self):
		nbrPlayer = 2
		nbrBall = 1

		self.stayInApp = True
		while self.stayInApp:
			self.frame.formPanel.displayForm(nbrPlayer, nbrBall)

			self.stayInForm = True
			while self.stayInForm:
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN:
						Mouse_x, Mouse_y = pygame.mouse.get_pos()
						if Mouse_y > self.frame.height * (2/3) - self.frame.formPanel.imgStartButton.get_height()/2 and Mouse_y < self.frame.height * (2/3) + self.frame.formPanel.imgStartButton.get_height()/2:
							if Mouse_x > self.frame.width * (2/3) - self.frame.formPanel.imgStartButton.get_width()/2 and Mouse_x < self.frame.width * (2/3) + self.frame.formPanel.imgStartButton.get_width()/2:
								self.initGame(nbrPlayer, nbrBall)
								self.startGame()
								self.stayInForm = False
							elif Mouse_x > self.frame.width * (1/3) - self.frame.formPanel.imgQuitButton.get_width()/2 and Mouse_x < self.frame.width * (1/3) + self.frame.formPanel.imgQuitButton.get_width()/2:
								self.stayInApp = False
								self.stayInForm = False
						elif Mouse_y > self.frame.height * (1/3) + self.frame.formPanel.imgDownButton.get_height() * 3/2 and Mouse_y < self.frame.height * (1/3) + self.frame.formPanel.imgDownButton.get_height() * 5/2:
							if Mouse_x > self.frame.width * (2/3) - self.frame.formPanel.imgUpButton.get_width() * 3/2 and Mouse_x < self.frame.width * (2/3) - self.frame.formPanel.imgUpButton.get_width() * 1/2 and nbrPlayer <= 1:
								nbrPlayer+=1
								self.frame.formPanel.refreshDisplaySelectionPlayerNbr(nbrPlayer)
							elif Mouse_x > self.frame.width * (2/3) + self.frame.formPanel.imgDownButton.get_width() * 1/2 and Mouse_x < self.frame.width * (2/3) + self.frame.formPanel.imgDownButton.get_width() * 3/2 and nbrPlayer >= 2:
								nbrPlayer-=1
								self.frame.formPanel.refreshDisplaySelectionPlayerNbr(nbrPlayer)
							elif Mouse_x > self.frame.width * (1/3) - self.frame.formPanel.imgUpButton.get_width() * 3/2 and Mouse_x < self.frame.width * (1/3) - self.frame.formPanel.imgUpButton.get_width() * 1/2 and nbrBall <= 4:
								nbrBall+=1
								self.frame.formPanel.refreshDisplaySelectionBallNbr(nbrBall)
							elif Mouse_x > self.frame.width * (1/3) + self.frame.formPanel.imgDownButton.get_width() * 1/2 and Mouse_x < self.frame.width * (1/3) + self.frame.formPanel.imgDownButton.get_width() * 3/2 and nbrBall >= 2:
								nbrBall-=1
								self.frame.formPanel.refreshDisplaySelectionBallNbr(nbrBall)
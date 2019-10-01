from pygame import *
from Player import *
from Ball import *
from PlayerController import *
from BallController import *

class Controller:

	pygame.init()
	continuer = True
	players = PlayerController(2)
	balls = BallController(5)
	ecran = pygame.display.set_mode((1000, 650))
	#ecran = pygame.display.set_mode((0, 0), FULLSCREEN)
	width = ecran.get_width()
	height = ecran.get_height()
	scoreRight = 0
	scoreLeft = 0

	def __init__(self):
		self.continuer = True

		self.players.CreatePlayers(self)
		self.balls.Createballs(self)

		pygame.display.set_caption("SoccerGame")
		icon = pygame.image.load("ressources/Soccer_Ball_icon.png")
		pygame.display.set_icon(icon)

	def startGame(self):
		while self.continuer:
			keystate = pygame.key.get_pressed()

			self.players.CheckKeyEventPLayers(keystate)

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_f:
						self.continuer = False
					if event.type == pygame.QUIT : 
						pygame.quit() 
						quit()
			
			for ball in self.balls.ballsList:
				for player in self.players.playersList:
					if ball.getX() > player.getX() and ball.getX() < player.getX() + player.getImgPlayer().get_width() and ball.getY() > player.getY() and ball.getY() < player.getY() + player.getImgPlayer().get_height() or ball.getX() + ball.getImgBall().get_width() > player.getX() and ball.getX() + ball.getImgBall().get_width() < player.getX() + player.getImgPlayer().get_width() and ball.getY() > player.getY() and ball.getY() < player.getY() + player.getImgPlayer().get_height() or ball.getX() + ball.getImgBall().get_width() > player.getX() and ball.getX() + ball.getImgBall().get_width() < player.getX() + player.getImgPlayer().get_width() and ball.getY() + ball.getImgBall().get_height() > player.getY() and ball.getY() + ball.getImgBall().get_height() < player.getY() + player.getImgPlayer().get_height() or ball.getX() > player.getX() and ball.getX() < player.getX() + player.getImgPlayer().get_width() and ball.getY() + ball.getImgBall().get_height() > player.getY() and ball.getY() + ball.getImgBall().get_height() < player.getY() + player.getImgPlayer().get_height():
						self.balls.collisionMovingObject(ball, player.getX() + player.getImgPlayer().get_width()/2, player.getY() + player.getImgPlayer().get_height()/2)
				
				for otherBall in self.balls.ballsList:
					if (ball.getX() > otherBall.getX() and ball.getX() < otherBall.getX() + otherBall.getImgBall().get_width() and ball.getY() > otherBall.getY() and ball.getY() < otherBall.getY() + otherBall.getImgBall().get_height() or ball.getX() + ball.getImgBall().get_width() > otherBall.getX() and ball.getX() + ball.getImgBall().get_width() < otherBall.getX() + otherBall.getImgBall().get_width() and ball.getY() > otherBall.getY() and ball.getY() < otherBall.getY() + otherBall.getImgBall().get_height() or ball.getX() + ball.getImgBall().get_width() > otherBall.getX() and ball.getX() + ball.getImgBall().get_width() < otherBall.getX() + otherBall.getImgBall().get_width() and ball.getY() + ball.getImgBall().get_height() > otherBall.getY() and ball.getY() + ball.getImgBall().get_height() < otherBall.getY() + otherBall.getImgBall().get_height() or ball.getX() > otherBall.getX() and ball.getX() < otherBall.getX() + otherBall.getImgBall().get_width() and ball.getY() + ball.getImgBall().get_height() > otherBall.getY() and ball.getY() + ball.getImgBall().get_height() < otherBall.getY() + otherBall.getImgBall().get_height()) and (ball.getX != otherBall.getX and ball.getX != otherBall.getX):
						self.balls.collisionMovingObject(ball, otherBall.getX() + otherBall.getImgBall().get_width()/2, otherBall.getY() + otherBall.getImgBall().get_height()/2)

				
				
			pygame.draw.rect(self.ecran, (255, 255, 255), (0, 0, self.width, self.height))

			for player in self.players.playersList:
				self.ecran.blit(player.getImgPlayer(), (player.getX(), player.getY()))
			
			for ball in self.balls.ballsList:
				self.balls.decelerate(ball)
				self.balls.collisionWall(ball, self)
				self.balls.move(ball)

				self.ecran.blit(ball.getImgBall(), (ball.getX(), ball.getY()))

			pygame.display.flip()
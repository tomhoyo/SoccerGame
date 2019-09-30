from pygame import *
from Player import *
from Ball import *

class Controller:

	pygame.init()
	continuer = True
	players = []
	balls = []
	ecran = pygame.display.set_mode((0, 0), FULLSCREEN)
	width = ecran.get_width()
	height = ecran.get_height()

	def __init__(self):
		self.continuer = True

		self.players.append(Player(self, 50, 200))
		self.balls.append(Ball(self, self.width/2, self.height/2))

		icon = pygame.image.load("ressources/Soccer_Ball_icon.png")

		pygame.display.set_caption("SoccerGame")
		pygame.display.set_icon(icon)

		pygame.draw.rect(self.ecran, (255, 255, 255), (0, 0, self.width, self.height))
		self.ecran.blit(self.players[0].imgPlayer, (self.players[0].getX(), self.players[0].getY()))

	def startGame(self):
		while self.continuer:
			keystate = pygame.key.get_pressed()
			if keystate[pygame.K_w] and self.players[0].getY() > 0:
				self.players[0].moveUp()
			if keystate[pygame.K_s] and self.players[0].getY() < self.players[0].limY:
				self.players[0].moveDown()
			if keystate[pygame.K_a] and self.players[0].getX() > 0:
				self.players[0].moveLeft()
			if keystate[pygame.K_d] and self.players[0].getX() < self.players[0].limX:
				self.players[0].moveRight()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_f:
						self.continuer = False
			
			for ball in self.balls:
				for player in self.players:
					if ball.getX() > player.getX() and ball.getX() < player.getX() + player.getImgPlayer().get_width() and ball.getY() > player.getY() and ball.getY() < player.getY() + player.getImgPlayer().get_height() or ball.getX() + ball.getImgBall().get_width() > player.getX() and ball.getX() + ball.getImgBall().get_width() < player.getX() + player.getImgPlayer().get_width() and ball.getY() > player.getY() and ball.getY() < player.getY() + player.getImgPlayer().get_height() or ball.getX() + ball.getImgBall().get_width() > player.getX() and ball.getX() + ball.getImgBall().get_width() < player.getX() + player.getImgPlayer().get_width() and ball.getY() + ball.getImgBall().get_height() > player.getY() and ball.getY() + ball.getImgBall().get_height() < player.getY() + player.getImgPlayer().get_height() or ball.getX() > player.getX() and ball.getX() < player.getX() + player.getImgPlayer().get_width() and ball.getY() + ball.getImgBall().get_height() > player.getY() and ball.getY() + ball.getImgBall().get_height() < player.getY() + player.getImgPlayer().get_height():
						ball.hurtPlayer(player.getX() + player.getImgPlayer().get_width()/2, player.getY() + player.getImgPlayer().get_height()/2)
				
				if ball.getX() > 0 and ball.getX() < ball.limX:
					ball.x += ball.speed * ball.dirX
					print("X: ", ball.dirX, " - ", ball.x)
					print("Y: ", ball.dirY, " - ", ball.y)
					print("--------------")
				"""else:
					ball.calculDir()"""

				if ball.getY() > 0 and ball.getY() < ball.limY:
					ball.y += ball.speed * ball.dirY

			pygame.draw.rect(self.ecran, (255, 255, 255), (0, 0, self.width, self.height))
			self.ecran.blit(self.players[0].getImgPlayer(), (self.players[0].getX(), self.players[0].getY()))
			self.ecran.blit(self.balls[0].getImgBall(), (self.balls[0].getX(), self.balls[0].getY()))

			pygame.display.flip()
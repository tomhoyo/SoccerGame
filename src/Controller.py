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
	scoreRight = 0
	scoreLeft = 0


	def __init__(self):
		self.continuer = True

		

		self.players.append(Player(self, 50, self.height/2))
		self.players.append(Player(self, self.width - 100, self.height/2))
		self.balls.append(Ball(self, self.width/2, self.height/2))
		#self.balls.append(Ball(self, self.width/2, self.height/2 + 70))

		icon = pygame.image.load("ressources/Soccer_Ball_icon.png")

		pygame.display.set_caption("SoccerGame")
		pygame.display.set_icon(icon)

		pygame.draw.rect(self.ecran, (255, 255, 255), (0, 0, self.width, self.height))
		self.ecran.blit(self.players[0].imgPlayer, (self.players[0].getX(), self.players[0].getY()))

	def startGame(self):
		while self.continuer:
			keystate = pygame.key.get_pressed()
			"""
			Player 1
			"""
			if keystate[pygame.K_w] and self.players[0].getY() > 0:
				self.players[0].moveUp()
			if keystate[pygame.K_s] and self.players[0].getY() < self.players[0].limY:
				self.players[0].moveDown()
			if keystate[pygame.K_a] and self.players[0].getX() > 0:
				self.players[0].moveLeft()
			if keystate[pygame.K_d] and self.players[0].getX() < self.players[0].limX:
				self.players[0].moveRight()

			"""
			Player 2
			"""
			if keystate[pygame.K_UP] and self.players[1].getY() > 0:
				self.players[1].moveUp()
			if keystate[pygame.K_DOWN] and self.players[1].getY() < self.players[1].limY:
				self.players[1].moveDown()
			if keystate[pygame.K_LEFT] and self.players[1].getX() > 0:
				self.players[1].moveLeft()
			if keystate[pygame.K_RIGHT] and self.players[1].getX() < self.players[1].limX:
				self.players[1].moveRight()


			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_f:
						self.continuer = False
					if event.type == pygame.QUIT : 
						pygame.quit() 
						quit()
			
			for ball in self.balls:
				for player in self.players:
					if ball.getX() > player.getX() and ball.getX() < player.getX() + player.getImgPlayer().get_width() and ball.getY() > player.getY() and ball.getY() < player.getY() + player.getImgPlayer().get_height() or ball.getX() + ball.getImgBall().get_width() > player.getX() and ball.getX() + ball.getImgBall().get_width() < player.getX() + player.getImgPlayer().get_width() and ball.getY() > player.getY() and ball.getY() < player.getY() + player.getImgPlayer().get_height() or ball.getX() + ball.getImgBall().get_width() > player.getX() and ball.getX() + ball.getImgBall().get_width() < player.getX() + player.getImgPlayer().get_width() and ball.getY() + ball.getImgBall().get_height() > player.getY() and ball.getY() + ball.getImgBall().get_height() < player.getY() + player.getImgPlayer().get_height() or ball.getX() > player.getX() and ball.getX() < player.getX() + player.getImgPlayer().get_width() and ball.getY() + ball.getImgBall().get_height() > player.getY() and ball.getY() + ball.getImgBall().get_height() < player.getY() + player.getImgPlayer().get_height():
						ball.hurtPlayer(player.getX() + player.getImgPlayer().get_width()/2, player.getY() + player.getImgPlayer().get_height()/2)
					
				ball.decelerate()

				if ball.getX() <= 0 or ball.getX() >= ball.limX:
					ball.hurtWallX()
					if ball.getX() >= ball.limX:
						self.scoreLeft += 1
					else:
						self.scoreRight += 1

				if ball.getY() <= 0 or ball.getY() >= ball.limY:
					ball.hurtWallY()

				ball.x += ball.speed * ball.dirX
				ball.y += ball.speed * ball.dirY

			print(self.scoreLeft , " - ", self.scoreRight)
				
			pygame.draw.rect(self.ecran, (255, 255, 255), (0, 0, self.width, self.height))

			for player in self.players:
				self.ecran.blit(player.getImgPlayer(), (player.getX(), player.getY()))
			
			for ball in self.balls:
				self.ecran.blit(ball.getImgBall(), (ball.getX(), ball.getY()))

			pygame.display.flip()
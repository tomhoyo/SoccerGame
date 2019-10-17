import pygame
from Frame import *

class GamePanel:
	frame = object
	width = 1366
	height = 768

	clock = pygame.time.Clock()
	frameRate = 300

	pygame.font.init()
	font = pygame.font.Font
	text = 0
	textRect = 0

	def __init__(self, frame):
		self.frame = frame
		self.width = frame.width
		self.height = frame.height

		self.font = pygame.font.Font('freesansbold.ttf', int(frame.height * 0.04))
		self.text = self.font.render('0 - 0', True, (255, 255, 255), (0, 0, 0))
		self.textRect = self.text.get_rect() 
		self.textRect.center = (frame.width // 2, int(frame.height * 0.04) / 2)

	def displayObjects(self, Objects):
		for Object in Objects.listObject:
			self.frame.frame.blit(Object.getImgSkin(), (Object.getX(), Object.getY()))

	def displayScore(self, scoreLeft, scoreRight):
		self.text = self.font.render(str(scoreLeft) + " - " + str(scoreRight), True, (255, 255, 255), (0, 0, 0))
		self.frame.frame.blit(self.text, self.textRect)

	def refreshGameFrame(self, balls, players, scoreLeft, scoreRight):
		self.clock.tick(self.frameRate)

		pygame.draw.rect(self.frame.frame, (255, 255, 255), (0, 0, self.width, self.height))
		self.displayScore(scoreLeft, scoreRight)
		self.displayObjects(balls)
		self.displayObjects(players)

		pygame.display.flip()

	def displayWinner(self, ctrl, winner):
		pygame.draw.rect(self.frame.frame, (255, 255, 255), (0, 0, self.width, self.height))

		font = pygame.font.Font('freesansbold.ttf', self.frame.height // 4)
		text = font.render("Winner : " + winner, True, (255, 255, 255), (0, 0, 0))
		textRect = text.get_rect() 
		textRect.center = (self.frame.width // 2, self.frame.height // 2)
		self.frame.frame.blit(text, textRect)


		self.displayScore(ctrl.scoreLeft, ctrl.scoreRight)
		pygame.display.flip()
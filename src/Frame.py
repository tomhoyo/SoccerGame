import pygame
from GamePanel import *
from FormPanel import *

class Frame:
	pygame.init()

	#frame = pygame.display.set_mode((1000, 650))
	frame = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

	width = 0
	height = 0

	gamePanel = object
	formPanel = object

	def __init__(self):
		pygame.display.set_caption("SoccerGame")
		pygame.display.set_icon(pygame.image.load("ressources/Soccer_Ball_icon.png"))

		self.width = self.frame.get_width()
		self.height = self.frame.get_height()

		self.gamePanel = GamePanel(self)
		self.formPanel = FormPanel(self)

	
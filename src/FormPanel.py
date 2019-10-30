import pygame

class FormPanel:
	frame = object
	width = 0
	height = 0

	imgQuitButton = pygame.image.load("ressources/quitgame.png")
	imgStartButton = pygame.image.load("ressources/startgame.png")
	imgUpButton = pygame.image.load("ressources/up.png")
	imgDownButton = pygame.image.load("ressources/down.png")

	rectNbrBall = 0
	rectNbrPlayer = 0

	def __init__(self, frame):
		self.frame = frame
		self.width = frame.width
		self.height = frame.height

	def displaySelectionPlayerNbr(self, nbrPlayer):
		self.imgUpButton = pygame.transform.scale(self.imgUpButton, (int(self.width * 0.02), int(self.height * 0.02)))
		self.frame.frame.blit(self.imgUpButton, (self.width * (1/3) - self.imgUpButton.get_width() * 3/2, self.height * (1/3) + self.imgUpButton.get_height() * 3/2))

		self.imgDownButton = pygame.transform.scale(self.imgDownButton, (int(self.width * 0.02), int(self.height * 0.02)))
		self.frame.frame.blit(self.imgDownButton, (self.width * (1/3) + self.imgDownButton.get_width() * 1/2, self.height * (1/3) + self.imgDownButton.get_height() * 3/2))

		font = pygame.font.Font('freesansbold.ttf', self.frame.height // 32)
		text = font.render("Choisez le nombre de joueur", True, (0, 0, 0), (255, 255, 255))
		textRect = text.get_rect()
		textRect.center = (self.frame.width * (2/3), self.frame.height * (1/3) - (self.frame.height // 32) * 3/2)
		self.frame.frame.blit(text, textRect)

		text = font.render(" " + str(nbrPlayer) + " ", True, (0, 0, 0), (255, 255, 255))
		textRect = text.get_rect()
		textRect.center = (self.frame.width * (2/3), self.frame.height * (1/3))
		self.frame.frame.blit(text, textRect)

	def refreshDisplaySelectionPlayerNbr(self, nbrPlayer):
		font = pygame.font.Font('freesansbold.ttf', self.frame.height // 32)
		text = font.render(" " + str(nbrPlayer) + " ", True, (0, 0, 0), (255, 255, 255))
		textRect = text.get_rect()
		textRect.center = (self.frame.width * (2/3), self.frame.height * (1/3))
		self.frame.frame.blit(text, textRect)
		pygame.display.flip()

	def displaySelectionBallNbr(self, nbrBall):
		self.imgUpButton = pygame.transform.scale(self.imgUpButton, (int(self.width * 0.02), int(self.height * 0.02)))
		self.frame.frame.blit(self.imgUpButton, (self.width * (2/3) - self.imgUpButton.get_width() * 3/2, self.height * (1/3) + self.imgUpButton.get_height() * 3/2))

		self.imgDownButton = pygame.transform.scale(self.imgDownButton, (int(self.width * 0.02), int(self.height * 0.02)))
		self.frame.frame.blit(self.imgDownButton, (self.width * (2/3) + self.imgDownButton.get_width() * 1/2, self.height * (1/3) + self.imgDownButton.get_height() * 3/2))

		font = pygame.font.Font('freesansbold.ttf', self.frame.height // 32)
		text = font.render("Choisez le nombre de balle", True, (0, 0, 0), (255, 255, 255))
		textRect = text.get_rect()
		textRect.center = (self.frame.width * (1/3), self.frame.height * (1/3) - (self.frame.height // 32) * 3/2)
		self.frame.frame.blit(text, textRect)

		text = font.render(" " + str(nbrBall) + " ", True, (0, 0, 0), (255, 255, 255))
		textRect = text.get_rect()
		textRect.center = (self.frame.width * (1/3), self.frame.height * (1/3))
		self.frame.frame.blit(text, textRect)

	def refreshDisplaySelectionBallNbr(self, nbrBall):
		font = pygame.font.Font('freesansbold.ttf', self.frame.height // 32)
		text = font.render(" " + str(nbrBall) + " ", True, (0, 0, 0), (255, 255, 255))
		textRect = text.get_rect()
		textRect.center = (self.frame.width * (1/3), self.frame.height * (1/3))
		self.frame.frame.blit(text, textRect)
		pygame.display.flip()

	def displayQuitGameButton(self):
		self.imgQuitButton = pygame.transform.scale(self.imgQuitButton, (int(self.width * 0.1), int(self.height * 0.05)))
		self.frame.frame.blit(self.imgQuitButton, (self.width * (1/3) - self.imgQuitButton.get_width()/2, self.height * (2/3) - self.imgQuitButton.get_height()/2))

	def displayStartGameButton(self):
		self.imgStartButton = pygame.transform.scale(self.imgStartButton, (int(self.width * 0.1), int(self.height * 0.05)))
		self.frame.frame.blit(self.imgStartButton, (self.width * (2/3) - self.imgStartButton.get_width()/2, self.height * (2/3) - self.imgStartButton.get_height()/2))

	def displayForm(self, nbrPlayer, nbrBall):
		pygame.draw.rect(self.frame.frame, (255, 255, 255), (0, 0, self.width, self.height))

		self.displayQuitGameButton()
		self.displayStartGameButton()

		self.displaySelectionBallNbr(nbrBall)
		self.displaySelectionPlayerNbr(nbrPlayer)
		
		pygame.display.flip()
			

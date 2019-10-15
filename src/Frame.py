import pygame

class Frame:

	pygame.init()

	#frame = pygame.display.set_mode((1000, 650))
	frame = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

	width = frame.get_width()
	height = frame.get_height()

	clock = pygame.time.Clock()
	frameRate = 300

	font = pygame.font.Font('freesansbold.ttf', int(height * 0.04))
	text = font.render('0 - 0', True, (255, 255, 255), (0, 0, 0))
	textRect = text.get_rect() 
	textRect.center = (width // 2, int(height * 0.04) / 2)

	def __init__(self):
		pygame.display.set_caption("SoccerGame")
		pygame.display.set_icon(pygame.image.load("ressources/Soccer_Ball_icon.png"))


	def displayObjects(self, Objects):
		for Object in Objects.listObject:
			self.frame.blit(Object.getImgSkin(), (Object.getX(), Object.getY()))

	def displayScore(self, scoreA, scoreB):
		self.text = self.font.render(str(scoreA) + " - " + str(scoreB), True, (255, 255, 255), (0, 0, 0))
		self.frame.blit(self.text, self.textRect) 


	def refreshFrame(self, balls, players, scoreA, scoreB):
		self.clock.tick(self.frameRate)

		pygame.draw.rect(self.frame, (255, 255, 255), (0, 0, self.width, self.height))

		self.displayScore(scoreA, scoreB)
		self.displayObjects(balls)
		self.displayObjects(players)

		pygame.display.flip()

	def displayForm():
		pass

	
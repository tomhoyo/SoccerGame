import pygame

class FormPanel:
	frame = object
	width = 0
	height = 0

	def __init__(self, frame):
		self.frame = frame
		self.width = frame.width
		self.height = frame.height

	def DisplaySelectionPLayerNbr(self):
		pass

	def DisplaySelectionBallNbr(self):
		pass

	def displayQuitGameButton(self):
		pass

	def displayStartGameButton(self):
		pass

	def displayForm(self):
		pygame.draw.rect(self.frame.frame, (255, 255, 255), (0, 0, self.width, self.height))

		"""
		placer les boutons
		"""
		pygame.display.flip()
			

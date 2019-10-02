from Player import *


class PlayerController:

	nbrPlayers = 0
	list = []


	def __init__(self, nbrPlayers):
		self.nbrPlayers = nbrPlayers

	def CreatePlayers(self, ctrl):
		if self.nbrPlayers >=1:
			self.list.append(Player(ctrl, 50, ctrl.frame.height/2))
		if self.nbrPlayers >= 2:
			self.list.append(Player(ctrl, ctrl.frame.width - 100, ctrl.frame.height/2))

	def CheckKeyEventPLayers(self, keystate):
		if self.nbrPlayers >=1:
			if keystate[pygame.K_w] and self.list[0].getY() > 0:
				self.list[0].moveUp()
			if keystate[pygame.K_s] and self.list[0].getY() < self.list[0].limY:
				self.list[0].moveDown()
			if keystate[pygame.K_a] and self.list[0].getX() > 0:
				self.list[0].moveLeft()
			if keystate[pygame.K_d] and self.list[0].getX() < self.list[0].limX:
				self.list[0].moveRight()
				
		if self.nbrPlayers >= 2:
			if keystate[pygame.K_UP] and self.list[1].getY() > 0:
				self.list[1].moveUp()
			if keystate[pygame.K_DOWN] and self.list[1].getY() < self.list[1].limY:
				self.list[1].moveDown()
			if keystate[pygame.K_LEFT] and self.list[1].getX() > 0:
				self.list[1].moveLeft()
			if keystate[pygame.K_RIGHT] and self.list[1].getX() < self.list[1].limX:
				self.list[1].moveRight()

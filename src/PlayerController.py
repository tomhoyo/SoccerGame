from Player import *


class PlayerController:

	nbrPlayers = 0
	playersList = []


	def __init__(self, nbrPlayers):
		self.nbrPlayers = nbrPlayers

	def CreatePlayers(self, ctrl):
		if self.nbrPlayers >=1:
			self.playersList.append(Player(ctrl, 50, ctrl.height/2))
		if self.nbrPlayers >= 2:
			self.playersList.append(Player(ctrl, ctrl.width - 100, ctrl.height/2))

	def CheckKeyEventPLayers(self, keystate):
		if self.nbrPlayers >=1:
			if keystate[pygame.K_w] and self.playersList[0].getY() > 0:
				self.playersList[0].moveUp()
			if keystate[pygame.K_s] and self.playersList[0].getY() < self.playersList[0].limY:
				self.playersList[0].moveDown()
			if keystate[pygame.K_a] and self.playersList[0].getX() > 0:
				self.playersList[0].moveLeft()
			if keystate[pygame.K_d] and self.playersList[0].getX() < self.playersList[0].limX:
				self.playersList[0].moveRight()
				
		if self.nbrPlayers >= 2:
			if keystate[pygame.K_UP] and self.playersList[1].getY() > 0:
				self.playersList[1].moveUp()
			if keystate[pygame.K_DOWN] and self.playersList[1].getY() < self.playersList[1].limY:
				self.playersList[1].moveDown()
			if keystate[pygame.K_LEFT] and self.playersList[1].getX() > 0:
				self.playersList[1].moveLeft()
			if keystate[pygame.K_RIGHT] and self.playersList[1].getX() < self.playersList[1].limX:
				self.playersList[1].moveRight()

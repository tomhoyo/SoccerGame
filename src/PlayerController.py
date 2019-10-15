from Player import *


class PlayerController:

	nbrPlayers = 0
	listObject = []
	listPos = []

	def __init__(self, nbrPlayers):
		self.nbrPlayers = nbrPlayers

	def CreatePlayers(self, ctrl):
		self.listPos.append([int(ctrl.frame.width * 0.036), ctrl.frame.height/2])
		self.listPos.append([ctrl.frame.width - int(ctrl.frame.width * 0.036), ctrl.frame.height/2])

		x = 0
		while x < self.nbrPlayers:
			self.listObject.append(Player(ctrl, self.listPos[x][0], self.listPos[x][1]))
			x+=1

	def CheckKeyEventPLayers(self, keystate):
		if self.nbrPlayers >=1:
			if keystate[pygame.K_w] and self.listObject[0].getY() > 0:
				self.listObject[0].moveUp()
			if keystate[pygame.K_s] and self.listObject[0].getY() < self.listObject[0].limY:
				self.listObject[0].moveDown()
			if keystate[pygame.K_a] and self.listObject[0].getX() > 0:
				self.listObject[0].moveLeft()
			if keystate[pygame.K_d] and self.listObject[0].getX() < self.listObject[0].limX:
				self.listObject[0].moveRight()
				
		if self.nbrPlayers >= 2:
			if keystate[pygame.K_UP] and self.listObject[1].getY() > 0:
				self.listObject[1].moveUp()
			if keystate[pygame.K_DOWN] and self.listObject[1].getY() < self.listObject[1].limY:
				self.listObject[1].moveDown()
			if keystate[pygame.K_LEFT] and self.listObject[1].getX() > 0:
				self.listObject[1].moveLeft()
			if keystate[pygame.K_RIGHT] and self.listObject[1].getX() < self.listObject[1].limX:
				self.listObject[1].moveRight()
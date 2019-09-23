import abc
import keyboard

from Block import *

class ShapeItem():
	def __init__(self, blocks):
		self.blocks = blocks
		self.gameBoard = None
		self.pile = None
		keyboard.on_press_key("left", self.moveLeftCB)
		keyboard.on_press_key("right", self.moveRightCB)
		keyboard.on_press_key("down", self.moveDownCB)
		keyboard.on_press_key("up", self.rotateCW)

	@abc.abstractmethod
	def rotateCW(self, event):
		pass

	@abc.abstractmethod
	def rotateCW(self, event):
		pass

	def registerGameBoard(self, gb):
		self.gameBoard = gb

	def registerPile(self, pile):
		self.pile = pile

	def moveDown(self):
		if self.gameBoard.canMoveDown(self) and self.pile.canMoveDown(self):
			for b in self.blocks:
				b.moveDown()
			return True
		else:
			return False

	def moveDownCB(self, event):
		if self.gameBoard.canMoveDown(self) and self.pile.canMoveDown(self):
			for b in self.blocks:
				b.moveDown()

	def moveLeftCB(self, event):
		if self.gameBoard.canMoveLeft(self) and self.pile.canMoveLeft(self):
			for b in self.blocks:
				b.moveLeft()

	def moveRightCB(self, event):
		if self.gameBoard.canMoveRight(self) and self.pile.canMoveRight(self):
			for b in self.blocks:
				b.moveRight()

	def show(self):
		for b in self.blocks:
			b.show(self.gameBoard)

	def getCoords(self):
		result = []
		for b in self.blocks:
			result.append(b.getCoords())
		return result

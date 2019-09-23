from graphics import *
from ShapeItem import *

class GameBoard(GraphWin):
	unitSize = 20
	def __init__(self, name, widthBlocks, heightBlocks):
		self.width = widthBlocks * self.unitSize
		self.height = heightBlocks * self.unitSize
		GraphWin.__init__(self, name, self.width, self.height, autoflush=False)

	def clear(win):
		for item in win.items[:]:
			item.undraw()
		win.update()

	def getUnitSize(self):
		return self.unitSize

	def getHeight(self):
		return int(self.height / self.unitSize)

	def getWidth(self):
		return int(self.width / self.unitSize)

	def canMoveDown(self, shapeItem):
		result = True
		coords = shapeItem.getCoords()
		for c in coords:
			if c.getY() == 0:
				result = False
		return result

	def canMoveRight(self, shapeItem):
		result = True
		coords = shapeItem.getCoords()
		for c in coords:
			if c.getX() >= self.getWidth() - 1:
				result = False
		return result

	def canMoveLeft(self, shapeItem):
		result = True
		coords = shapeItem.getCoords()
		for c in coords:
			if c.getX() <= 0:
				result = False
		return result

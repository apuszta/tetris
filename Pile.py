from ShapeItem import *

class Pile:
	def __init__(self, width, height):
		self.blocks = [[0] * width for i in range(height)]
		self.width = width
		self.height = height

	def merge(self, shapeItem):
		coords = shapeItem.getCoords()
		for c in coords:
			self.blocks[int(c.getY())][int(c.getX())] = 1

	def canMoveDown(self, shapeItem):
		result = True
		coords = shapeItem.getCoords()
		for c in coords:
			if self.blocks[int(c.getY() - 1)][int(c.getX())] == 1:
				result = False
		return result

	def canMoveLeft(self, shapeItem):
		result = True
		coords = shapeItem.getCoords()
		for c in coords:
			if self.blocks[int(c.getY())][int(c.getX() - 1)] == 1:
				result = False
		return result

	def canMoveRight(self, shapeItem):
		result = True
		coords = shapeItem.getCoords()
		for c in coords:
			if self.blocks[int(c.getY())][int(c.getX() + 1)] == 1:
				result = False
		return result

	def clearFullLines(self):
		fullLines = []
		for i in range(0,self.height):
			if sum(self.blocks[i]) == self.width:
				fullLines.append(i)
		while fullLines:
			for i in range(fullLines[0], self.height-1):
				self.blocks[i] = self.blocks[i+1]
			self.blocks[self.height-1] = [0] * self.width
			for index in range(0,len(fullLines)):
				fullLines[index] -= 1
			fullLines.pop(0)

	def show(self, window):
		for row in range(0,self.height):
			for col in range(0,self.width):
				if self.blocks[row][col] == 1:
					unitSize = window.getUnitSize()
					offset = unitSize
					rectangle = Rectangle(
						Point(unitSize * col, unitSize * (window.getHeight() - row) - offset),
						Point(unitSize * col + offset, unitSize * (window.getHeight() - row))
					)
					rectangle.setFill('blue')
					rectangle.draw(window)

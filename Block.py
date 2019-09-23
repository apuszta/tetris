from graphics import *

class Block:
	def __init__(self, xinit, yinit):
		self.x = xinit
		self.y = yinit

	def show(self, window):
		unitSize = window.getUnitSize()
		offset = unitSize
		rectangle = Rectangle(
			Point(unitSize * self.x, unitSize * (window.getHeight() - self.y) - offset),
			Point(unitSize * self.x + offset, unitSize * (window.getHeight() - self.y))
		)
		rectangle.setFill('red')
		rectangle.draw(window)

	def moveDown(self, amount=1):
		self.y -= amount * 1
		return self

	def moveUp(self, amount=1):
		self.y += amount * 1
		return self

	def moveRight(self, amount=1):
		self.x += amount * 1
		return self

	def moveLeft(self, amount=1):
		self.x -= amount * 1
		return self

	def getCoords(self):
		return Point(self.x, self.y)

from ShapeItem import *

class SShape(ShapeItem):
	def __init__(self, centerX, centerY):
		b0 = Block(centerX, centerY)
		b1 = Block(centerX + 1, centerY)
		b2 = Block(centerX - 1, centerY - 1)
		b3 = Block(centerX, centerY - 1)
		ShapeItem.__init__(self, [b0, b1, b2, b3])
		self.orientation = 0

	def rotateCW(self, event):
		if self.orientation == 0:
			self.blocks[1].moveDown().moveLeft()
			self.blocks[2].moveUp().moveUp()
			self.blocks[3].moveLeft().moveUp()
			self.orientation = 1
		elif self.orientation == 1:
			self.blocks[1].moveRight().moveUp()
			self.blocks[2].moveDown().moveDown()
			self.blocks[3].moveDown().moveRight()
			self.orientation = 0

	def rotateCCW(self, event):
		self.rotateCW()

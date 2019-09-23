from ShapeItem import *

class LineShape(ShapeItem):
	def __init__(self, centerX, centerY):
		b0 = Block(centerX, centerY)
		b1 = Block(centerX - 1, centerY)
		b2 = Block(centerX + 1, centerY)
		b3 = Block(centerX + 2, centerY)
		ShapeItem.__init__(self, [b0, b1, b2, b3])
		self.orientation = 0

	def rotateCW(self, event):
		if self.orientation == 0:
			self.blocks[1].moveUp().moveRight()
			self.blocks[2].moveDown().moveLeft()
			self.blocks[3].moveDown().moveDown().moveLeft().moveLeft()
			self.orientation = 1
		elif self.orientation == 1:
			self.blocks[1].moveLeft().moveDown()
			self.blocks[2].moveRight().moveUp()
			self.blocks[3].moveRight().moveRight().moveUp().moveUp()
			self.orientation = 0

	def rotateCCW(self, event):
		self.rotateCW()

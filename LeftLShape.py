from ShapeItem import *

class LeftLShape(ShapeItem):
	def __init__(self, centerX, centerY):
		b0 = Block(centerX, centerY)
		b1 = Block(centerX, centerY - 1)
		b2 = Block(centerX, centerY - 2)
		b3 = Block(centerX - 1, centerY - 2)
		ShapeItem.__init__(self, [b0, b1, b2, b3])
		self.orientation = 0

	def rotateCW(self, event):
		if self.orientation == 0:
			self.blocks[0].moveRight().moveDown()
			self.blocks[2].moveLeft().moveUp()
			self.blocks[3].moveUp().moveUp()
			self.orientation = 1
		elif self.orientation == 1:
			self.blocks[0].moveDown().moveLeft()
			self.blocks[2].moveUp().moveRight()
			self.blocks[3].moveRight().moveRight()
			self.orientation = 2
		elif self.orientation == 2:
			self.blocks[0].moveLeft().moveUp()
			self.blocks[2].moveRight().moveDown()
			self.blocks[3].moveDown().moveDown()
			self.orientation = 3
		elif self.orientation == 3:
			self.blocks[0].moveUp().moveRight()
			self.blocks[2].moveDown().moveLeft()
			self.blocks[3].moveLeft().moveLeft()
			self.orientation = 0

	def rotateCCW(self, event):
		if self.orientation == 0:
			self.blocks[0].moveLeft().moveDown()
			self.blocks[2].moveRight().moveUp()
			self.blocks[3].moveRight().moveRight()
			self.orientation = 3
		elif self.orientation == 1:
			self.blocks[0].moveUp().moveLeft()
			self.blocks[2].moveDown().moveRight()
			self.blocks[3].moveDown().moveDown()
			self.orientation = 0
		elif self.orientation == 2:
			self.blocks[0].moveRight().moveUp()
			self.blocks[2].moveLeft().moveDown()
			self.blocks[3].moveLeft().moveLeft()
			self.orientation = 1
		elif self.orientation == 3:
			self.blocks[0].moveDown().moveRight()
			self.blocks[2].moveUp().moveLeft()
			self.blocks[3].moveUp().moveUp()
			self.orientation = 2

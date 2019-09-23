from ShapeItem import *

class OShape(ShapeItem):
	def __init__(self, centerX, centerY):
		b0 = Block(centerX, centerY)
		b1 = Block(centerX + 1, centerY)
		b2 = Block(centerX, centerY - 1)
		b3 = Block(centerX + 1, centerY - 1)
		ShapeItem.__init__(self, [b0, b1, b2, b3])

	def rotateCW(self, event):
		pass

	def rotateCCW(self, event):
		pass

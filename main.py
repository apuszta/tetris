import time
import random

from TShape import *
from RightLShape import *
from LeftLShape import *
from OShape import *
from SShape import *
from ZShape import *
from LineShape import *
from GameBoard import *
from Pile import *

def generateRandomShape(x,y):
	# select from shapes: rL, lL, line, Z, S, O, T
	selection = random.randrange(7)
	if selection == 0:
		return RightLShape(x,y)
	elif selection == 1:
		return LeftLShape(x,y)
	elif selection == 2:
		return LineShape(x,y)
	elif selection == 3:
		return ZShape(x,y)
	elif selection == 4:
		return SShape(x,y)
	elif selection == 5:
		return OShape(x,y)
	elif selection == 6:
		return TShape(x,y)

def main():
	boardWidth = 15
	boardHeight = 40

	shape = None
	gb = GameBoard("Game area", boardWidth, boardHeight)
	pile = Pile(boardWidth,boardHeight)

	play = True
	while play:
		gb.clear()
		if shape is not None:
			if shape.moveDown():
				shape.show()
			else:
				pile.merge(shape)
				pile.clearFullLines()
				shape = generateRandomShape(int(boardWidth / 2), boardHeight - 2)
				shape.registerGameBoard(gb)
				shape.registerPile(pile)
		else:
			shape = generateRandomShape(int(boardWidth / 2), boardHeight - 2)
			shape.registerGameBoard(gb)
			shape.registerPile(pile)
		pile.show(gb)
		gb.update()
		time.sleep(0.3)

main()
input("press enter to finish.")

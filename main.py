from modules.Board import Board
from modules.Utils import FENParser
from modules.BoardASCIIRenderer import BoardASCIIRenderer
import pprint


board = Board()
renderer = BoardASCIIRenderer()
print()
pprint.pprint(board.board)

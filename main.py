from modules.Board import Board
from modules.Utils import FENParser
from modules.BoardASCIIRenderer import BoardASCIIRenderer
import pprint


board = Board("k7/8/8/8/8/8/R7/1Q6 w - - 0 1")
renderer = BoardASCIIRenderer()
print(renderer.render(board.board))

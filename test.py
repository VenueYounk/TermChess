from modules.Board import Board
from modules.BoardASCIIRenderer import BoardASCIIRenderer

board = Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
renderer = BoardASCIIRenderer()
print(renderer.render(board.board))

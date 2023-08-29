from ..Coords import ChessCoord
from ..Pieces import Bishop, King, Knight, Pawn, Queen, Rook


class Board:
    def _create_default_board():
        board = {}
        # Set the initial positions of the pieces
        for y in [1, 8]:
            color = "white" if y == 1 else "black"
            board[ChessCoord(1, y)] = Rook(color)
            board[ChessCoord(2, y)] = Knight(color)
            board[ChessCoord(3, y)] = Bishop(color)
            board[ChessCoord(4, y)] = Queen(color)
            board[ChessCoord(5, y)] = King(color)
            board[ChessCoord(6, y)] = Bishop(color)
            board[ChessCoord(7, y)] = Knight(color)
            board[ChessCoord(8, y)] = Rook(color)
        for x in range(1, 9):
            board[ChessCoord(x, 2)] = Pawn("white")
            board[ChessCoord(x, 7)] = Pawn("black")
        return board

    def __init__(self, board=_create_default_board()):
        self.board = board

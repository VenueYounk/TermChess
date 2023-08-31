from ..Coords import ChessCoord
from ..Pieces import Bishop, King, Knight, Pawn, Queen, Rook
from ..Utils import FENParser


class Board:
    default_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

    def __init__(self, fen_board=default_fen):
        """
        self.board = {
            ChessCord : Piece,
            ChessCord : Piece,
            ChessCord : Piece,
            ChessCord : Piece,
            ChessCord : Piece,
        }
        """

        self.board = FENParser.parse(fen_board)

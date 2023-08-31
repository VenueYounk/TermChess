from ..Coords import ChessCoord
from ..Pieces import Bishop, King, Knight, Pawn, Queen, Rook
from ..Utils import FENParser


class Board:
    default_fen = "r1bqkb1r/ppp2ppp/2n3K1/3pp3/3PP3/1BN2N2/PPP2PPP/R1BQ3R w HAkq - 0 1"

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

    def has_piece(self, x, y):
        if ChessCoord(x, y) in self.board:
            return self.board[ChessCoord(x, y)]
        return False

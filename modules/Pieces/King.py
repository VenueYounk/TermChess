from .Piece import Piece
from ..Coords import ChessCoordShift


class King(Piece):
    name = "King"

    def __init__(self, color):
        self.color = color

    def get_avaible_moves(self, board):
        avaible_moves = []

        potentional_moves = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx != 0 or dy != 0:
                    potentional_moves.append(ChessCoordShift(dx, dy))

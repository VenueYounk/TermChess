from .Piece import Piece


class Pawn(Piece):
    name = "Pawn"

    def __init__(self, color):
        self.color = color

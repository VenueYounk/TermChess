from .Piece import Piece


class Rook(Piece):
    name = "Rook"

    def __init__(self, color):
        self.color = color

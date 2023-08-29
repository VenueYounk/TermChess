from .Piece import Piece


class Knight(Piece):
    name = "Knight"

    def __init__(self, color):
        self.color = color

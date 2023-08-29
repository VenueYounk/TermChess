from .Piece import Piece


class Bishop(Piece):
    name = "Bishop"

    def __init__(self, color):
        self.color = color

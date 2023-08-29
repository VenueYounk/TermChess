from .Piece import Piece


class Queen(Piece):
    name = "Queen"

    def __init__(self, color):
        self.color = color

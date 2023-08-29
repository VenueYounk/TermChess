from .Piece import Piece


class King(Piece):
    name = "King"

    def __init__(self, color):
        self.color = color

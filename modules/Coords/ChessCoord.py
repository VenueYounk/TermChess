from .ChessCoordShift import ChessCoordShift
from .Coord import Coord


class ChessCoord(Coord):
    LETTERS = {
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H",
    }

    def __iadd__(self, shift):
        if isinstance(shift, ChessCoordShift):
            self.x += shift.x
            self.y += shift.y
            return self
        raise TypeError("Unsupported operation")

    def __isub__(self, shift):
        if isinstance(shift, ChessCoordShift):
            self.x -= shift.x
            self.y -= shift.y
            return self
        raise TypeError("Unsupported operation")

    def __repr__(self):
        return f"{self.LETTERS[self.x]}{self.y}"

    def __str__(self):
        return f"{self.LETTERS[self.x]}{self.y}"

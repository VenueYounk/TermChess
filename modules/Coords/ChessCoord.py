from .ChessCoordShift import ChessCoordShift
from .Coord import Coord


class ChessCoord(Coord):
    LETTERS = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F",
        6: "G",
        7: "H",
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
        return f"{self.LETTERS[self.x]}{self.y + 1}"

    def __str__(self):
        return f"{self.LETTERS[self.x]}{self.y + 1}"

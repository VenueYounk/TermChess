from ..Pieces import *
from ..Coords import ChessCoord

# TO-DO
# 1.1 Error handler for incorrect FEN / FEN Validator
# 1.2 FEN generator


class FENParser:
    def parse(fen):
        """
        Parses the given FEN string and returns a dictionary representing the chessboard.
        !!! Now returns only the position on the board !!!

        Args:
            fen (str): The FEN string representing the current chessboard state.

        Returns:
            dict: A dictionary representing the chessboard,
            where the keys are tuples representing the position on the board (column, row)
            and the values are the corresponding chess pieces.

        Example:
            >>> fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
            >>> parse(fen)
            {
                (1, 8): Rook("black"),
                (2, 8): Knight("black"),
                (3, 8): Bishop("black"),
                ...
                (8, 1): Rook("white"),
                (7, 1): Knight("white"),
                (6, 1): Bishop("white"),
                ...
            }
        """
        position, turn, castling, en_passant, halfmove, fullmove = fen.split()

        def expand_empty_spaces(segment):
            return "".join(
                [" " * int(char) if char.isdigit() else char for char in segment]
            )

        position = expand_empty_spaces(position)
        rows = position.split("/")

        chessboard = {}

        for row_num, row in enumerate(rows):
            col_num = 1
            for char in row:
                if char.isdigit():
                    col_num += int(char)
                else:
                    color = "white" if char.isupper() else "black"
                    piece_type = char.lower()

                    if piece_type == "p":
                        piece = Pawn(color)
                    elif piece_type == "n":
                        piece = Knight(color)
                    elif piece_type == "b":
                        piece_type = Bishop(color)
                    elif piece_type == "r":
                        piece = Rook(color)
                    elif piece_type == "q":
                        piece = Queen(color)
                    elif piece_type == "k":
                        piece = King(color)

                    chessboard[ChessCoord(col_num, 8 - row_num)] = piece
                    col_num += 1

        return chessboard

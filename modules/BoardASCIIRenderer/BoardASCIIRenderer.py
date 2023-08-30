from ..Pieces import Bishop, King, Knight, Pawn, Queen, Rook
from colorama import Back, Style
from ..Coords import ChessCoord
from ..Pieces import Piece
from ..Board import Board


# init должен принимать экземпляр класса board


class BoardASCIIRenderer:
    ASCII_PIECE = {
        Pawn: "♟",
        Knight: "♞",
        Bishop: "♝",
        Rook: "♜",
        Queen: "♛",
        King: "♚"
    }

    ASCII_COLOR = {
        "black": "\033[31m",
        "white": "\033[37m"
    }

    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]

    def render(self, chess_dict):
        board_str = ""
        for position, piece in chess_dict.items():
            row, col = position.y, position.x
            self.board[row][col] = piece

        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    board_str += Back.WHITE
                else:
                    board_str += Back.BLACK

                square_piece = self.board[row][col]
                if square_piece is not None:
                    board_str += f"{self.ASCII_COLOR[square_piece.color]} {self.ASCII_PIECE[square_piece.__class__]}  "
                else:
                    board_str += "    "
            board_str += Style.RESET_ALL + "\n"
        return board_str





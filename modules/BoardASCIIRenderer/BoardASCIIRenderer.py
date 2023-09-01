from ..Pieces import Bishop, King, Knight, Pawn, Queen, Rook
from colorama import Back, Style


class BoardASCIIRenderer:
    ASCII_PIECE = {
        Pawn: "♟",
        Knight: "♞",
        Bishop: "♝",
        Rook: "♜",
        Queen: "♛",
        King: "♚",
    }

    ASCII_COLOR = {"black": "\033[31m", "white": "\033[37m"}

    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]

    def render(self, chess_dict, move_history):
        board_str = ""

        for position, piece in chess_dict.items():
            row, col = position.y, position.x
            self.board[7 - row][col] = piece

        for row in range(8):
            board_str += f"{8 - row} "
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

            board_str += Style.RESET_ALL
            if row == 0:
                board_str += "    MOVES HISTORY"

            elif row < len(move_history):
                move = move_history[row]
                board_str += f"    {move['white']: <6}:  {move['black']: <6}" if 'black' in move else f"    {move['white']: <6}: "

            board_str += "\n"

        board_str += "   A   B   C   D   E   F   G   H\n"

        return board_str


print("\033[H\033[J")

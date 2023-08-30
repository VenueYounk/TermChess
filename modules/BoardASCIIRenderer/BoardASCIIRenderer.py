from ..Pieces import Bishop, King, Knight, Pawn, Queen, Rook
from colorama import Back, Style

# init должен принимать экземпляр класса board
# входные данные фигура с цветом, встает автоматически на свое место


class BoardASCIIRenderer:
    ascii_pieces = {
        Pawn: "♟",
        Knight: "♞",
        Bishop: "♝",
        Rook: "♜",
        Queen: "♛",
        King: "♚"
    }

    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]

    def render(self, chess_dict):
        board_str = ""
        for position, piece in chess_dict.items():
            row, col = position
            self.board[row][col] = piece

        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    board_str += Back.WHITE
                else:
                    board_str += Back.BLACK

                square_content = self.board[row][col]
                if square_content is not None:
                    board_str += f" {square_content}  "
                else:
                    board_str += "    "
            board_str += Style.RESET_ALL + "\n"
        return board_str

color = {
    "black":"\033[31m",
    "white":"\033[37m"
}


print("\033[H\033[J")

board = BoardASCIIRenderer()
chess_dict = {
    (ChessCord): color[piece.color] + ascii_pieces[piece] 
    (0, 0): R + "♜",
    (0, 1): R + "♞",
    (0, 2): R + "♝",
    (0, 3): R + "♛",
    (0, 4): R + "♚",
    (0, 5): R + "♝",
    (0, 6): R + "♞",
    (0, 7): R + "♜",
    (1, 0): R + "♟",
    (1, 1): R + "♟",
    (1, 2): R + "♟",
    (1, 3): R + "♟",
    (1, 4): R + "♟",
    (1, 5): R + "♟",
    (1, 6): R + "♟",
    (1, 7): R + "♟",
    (6, 0): W + "♟",
    (6, 1): W + "♟",
    (6, 2): W + "♟",
    (6, 3): W + "♟",
    (6, 4): W + "♙",
    (6, 5): W + "♙",
    (6, 6): W + "♙",
    (6, 7): W + "♙",
    (7, 0): W + "♖",
    (7, 1): W + "♘",
    (7, 2): W + "♗",
    (7, 3): W + "♕",
    (7, 4): W + "♔",
    (7, 5): W + "♗",
    (7, 6): W + "♘",
    (7, 7): W + "♖",
}
board.render(chess_dict)
print(board.render(chess_dict))

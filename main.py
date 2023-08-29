from modules.Board import Board
import pprint

board = Board()


# pprint.pprint(board.board, indent=4)


def generate_chess_board(size=8):
    for row in range(size):
        for col in range(size):
            if (row + col) % 2 == 0:
                print("██", end="")
            else:
                print("  ", end="")
        print()


# Вызов функции для создания доски размером 8x8
generate_chess_board()

from .Piece import Piece
from ..Coords import ChessCoordShift, ChessCoord


class King(Piece):
    name = "King"

    def __init__(self, color):
        self.color = color

    def generate_moves(self):
        moves = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx != 0 or dy != 0:
                    moves.append(ChessCoordShift(dx, dy))
        return moves

    def get_avaible_moves(self, board, position):
        available_moves = []
        potentional_moves = self.generate_moves()
        for position_shift in potentional_moves:
            new_x, new_y = position.x + position_shift.x, position.y + position_shift.y
            # Проверка находится ли новая позиция на доске (предположим, доска 8x8)
            if 0 <= new_x <= 7 and 0 <= new_y <= 7:
                # Проверка наличия другой фигуры на новой позиции
                pieces_at_new_position = board.has_piece(new_x, new_y)
                if (
                    not pieces_at_new_position
                    or pieces_at_new_position.color != self.color
                ):
                    available_moves.append(ChessCoord(new_x, new_y))
        return available_moves

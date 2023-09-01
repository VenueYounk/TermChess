from modules.Board import Board
from modules.BoardASCIIRenderer import BoardASCIIRenderer

move_history = [
    {
        "white": "f5",
        "black": "e6"
    },
    {
        "white": "fxe6",
        "black": "fxe6"
    },
    {
        "white": "Nb5",
        "black": "c6"
    },
    {
        "white": "Nc7+",
        "black": "Ke7"
    },
    {
        "white": "Nxa8",
        "black": "b6"
    },
    {
        "white": "b5",
        "black": "cxb5"
    },
    {
        "white": "Nxb6",
        "black": "Nc6"
    },
    {
        "white": "Nxc8+",
    }
]

board = Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
renderer = BoardASCIIRenderer()
print(renderer.render(board.board, move_history))



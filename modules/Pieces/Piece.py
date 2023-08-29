from abc import ABC, abstractmethod


class Piece(ABC):
    name = "Piece"

    def __init__(self, color) -> None:
        self.color = color

    def __repr__(self) -> str:
        return f"{self.name} {self.color} "

    def __str__(self) -> str:
        return f"{self.name} {self.color} "

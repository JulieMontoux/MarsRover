from enum import Enum
from .direction import Direction

class Mouvement:
    MOUVEMENTS = {
        Direction.N: (0, -1),
        Direction.E: (1, 0),
        Direction.S: (0, 1),
        Direction.W: (-1, 0)
    }

    @staticmethod
    def get_movement(direction):
        return Mouvement.MOUVEMENTS[direction]

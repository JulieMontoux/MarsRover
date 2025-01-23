from enum import Enum

class Direction(Enum):
    N = 'N'
    E = 'E'
    S = 'S'
    W = 'W'

    MOUVEMENTS = {
        N: (0, -1),
        E: (1, 0),
        S: (0, 1),
        W: (-1, 0)
    }

    @staticmethod
    def tourner_a_gauche(direction):
        directions = [Direction.N, Direction.W, Direction.S, Direction.E]
        index = directions.index(direction)
        return directions[(index - 1) % len(directions)]

    @staticmethod
    def tourner_a_droite(direction):
        directions = [Direction.N, Direction.E, Direction.S, Direction.W]
        index = directions.index(direction)
        return directions[(index + 1) % len(directions)]

    @staticmethod
    def get_movement(direction):
        if not isinstance(direction, Direction):
            raise TypeError(f"direction doit être une instance de Direction, mais a reçu {type(direction)}.")
        return Direction.MOUVEMENTS[direction.value]

from enum import Enum

# Fournit des services statiques pour gérer les orientations du rover.
# Inclut les calculs de rotation (gauche/droite) et les deltas associés pour le déplacement en fonction de la direction actuelle.
class Direction(Enum):
    N = 'N'
    E = 'E'
    S = 'S'
    W = 'W'

    @staticmethod
    def tourner_a_gauche(direction):
        directions = [Direction.N, Direction.W, Direction.S, Direction.E]
        index = directions.index(direction)
        return directions[(index + 1) % len(directions)]

    @staticmethod
    def tourner_a_droite(direction):
        directions = [Direction.N, Direction.E, Direction.S, Direction.W]
        index = directions.index(direction)
        return directions[(index + 1) % len(directions)]

    @staticmethod
    def get_delta(direction):
        deltas = {
            Direction.N: (0, -1),
            Direction.E: (1, 0),
            Direction.S: (0, 1),
            Direction.W: (-1, 0),
        }
        return deltas[direction]

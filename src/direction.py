from enum import Enum

class Direction(Enum):
    N = 'N'
    E = 'E'
    S = 'S'
    W = 'W'

    @staticmethod
    def tourner_a_gauche(direction):
        directions = list(Direction)
        index = directions.index(direction)
        return directions[(index - 1) % len(directions)]

    @staticmethod
    def tourner_a_droite(direction):
        directions = list(Direction)
        index = directions.index(direction)
        return directions[(index + 1) % len(directions)]

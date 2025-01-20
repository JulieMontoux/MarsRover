import abc
from etat_rover import EtatRover

class Rover:
    DIRECTIONS = ['N', 'E', 'S', 'O']
    MOVEMENTS = {
        'N': (0, -1),
        'E': (1, 0),
        'S': (0, 1),
        'O': (-1, 0)
    }

    def __init__(self, x, y, orientation, planete):
        self.position = EtatRover(x, y, orientation)
        self.planete = planete

    def avancer(self):
        dx, dy = self.MOVEMENTS[self.position.orientation]
        self.position.x = (self.position.x + dx) % self.planete[0]
        self.position.y = (self.position.y + dy) % self.planete[1]

    def reculer(self):
        dx, dy = self.MOVEMENTS[self.position.orientation]
        self.position.x = (self.position.x - dx) % self.planete[0]
        self.position.y = (self.position.y - dy) % self.planete[1]

    def tourner_a_gauche(self):
        index = self.DIRECTIONS.index(self.position.orientation)
        self.position.orientation = self.DIRECTIONS[(index - 1) % 4]

    def tourner_a_droite(self):
        index = self.DIRECTIONS.index(self.position.orientation)
        self.position.orientation = self.DIRECTIONS[(index + 1) % 4]

    def get_position(self):
        return f"Position: ({self.position.x}, {self.position.y}), Orientation: {self.position.orientation}"

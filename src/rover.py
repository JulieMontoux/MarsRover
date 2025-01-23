from etat_rover import EtatRover
from direction import Direction
from mouvement import Mouvement

class Rover:
    def __init__(self, x, y, orientation, planete):
        self.position = EtatRover(x, y, Direction(orientation))
        self.planete = planete 

    def avancer(self):
        dx, dy = Mouvement[self.position.orientation.value].value
        self.position.x = (self.position.x + dx) % self.planete[0]
        self.position.y = (self.position.y + dy) % self.planete[1]

    def reculer(self):
        dx, dy = Mouvement[self.position.orientation.value].value
        self.position.x = (self.position.x - dx) % self.planete[0]
        self.position.y = (self.position.y - dy) % self.planete[1]

    def tourner_a_gauche(self):
        directions = list(Direction)
        index = directions.index(self.position.orientation)
        self.position.orientation = directions[(index - 1) % len(directions)]

    def tourner_a_droite(self):
        directions = list(Direction)
        index = directions.index(self.position.orientation)
        self.position.orientation = directions[(index + 1) % len(directions)]

    def get_position(self):
        return f"Position: ({self.position.x}, {self.position.y}), Orientation: {self.position.orientation.value}"
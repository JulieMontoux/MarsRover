from .mouvement import Mouvement
from .direction import Direction

class EtatRover:
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def avancer(self, planete):
        dx, dy = Mouvement.get_movement(self.orientation)
        self.x = (self.x + dx) % planete[0]
        self.y = (self.y + dy) % planete[1]

    def reculer(self, planete):
        dx, dy = Mouvement.get_movement(self.orientation)
        self.x = (self.x - dx) % planete[0]
        self.y = (self.y - dy) % planete[1]

    def tourner_a_gauche(self):
        self.orientation = Direction.tourner_a_gauche(self.orientation)

    def tourner_a_droite(self):
        self.orientation = Direction.tourner_a_droite(self.orientation)

    def get_position(self):
        return f"Position: ({self.x}, {self.y}), Orientation: {self.orientation.value}"

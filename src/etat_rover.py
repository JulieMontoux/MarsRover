from .position import Position
from .direction import Direction

class EtatRover:
    def __init__(self, x, y, orientation):
        self.position = Position(x, y)
        self.orientation = orientation

    def avancer(self, planete):
        dx, dy = Direction.get_movement(self.orientation)
        self.position.deplacer(dx, dy, planete)

    def reculer(self, planete):
        dx, dy = Direction.get_movement(self.orientation)
        self.position.deplacer(-dx, -dy, planete)

    def tourner_a_gauche(self):
        self.orientation = Direction.tourner_a_gauche(self.orientation)

    def tourner_a_droite(self):
        self.orientation = Direction.tourner_a_droite(self.orientation)

    def get_position(self):
        x, y = self.position.get_coords()
        return f"Position: ({x}, {y}), Orientation: {self.orientation.value}"

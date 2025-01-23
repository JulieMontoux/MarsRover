from .position import Position
from .direction import Direction

# Représente une entité composite combinant la position et l'orientation du rover.
# Cette classe centralise les déplacements et rotations pour éviter que la logique soit dispersée dans plusieurs classes.
class EtatRover:
    def __init__(self, x, y, orientation):
        self.position = Position(x, y)
        self.orientation = Direction[orientation]

    def deplacer(self, mouvement, planete):
        dx, dy = Direction.get_delta(self.orientation)
        if mouvement == 'R':
            dx, dy = -dx, -dy
        self.position.deplacer(dx, dy, planete)

    def tourner(self, direction):
        if direction == 'G':
            self.orientation = Direction.tourner_a_gauche(self.orientation)
        elif direction == 'D':
            self.orientation = Direction.tourner_a_droite(self.orientation)

    def get_position(self):
        x, y = self.position.get_coords()
        return x, y, self.orientation.name

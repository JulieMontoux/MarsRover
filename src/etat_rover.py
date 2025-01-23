from .direction import Direction
from .position import Position

# Représente une entité composite combinant la position et l'orientation du rover.
# Cette classe centralise les déplacements et rotations pour éviter que la logique soit dispersée dans plusieurs classes.
class EtatRover:
    def __init__(self, position, orientation):
        self._position = position
        self._orientation = orientation

    def deplacer(self, mouvement, planete):
        dx, dy = Direction.get_delta(self._orientation)
        if mouvement == 'R':
            dx, dy = -dx, -dy
        new_position = self._position.deplacer(dx, dy, planete)
        return EtatRover(new_position, self._orientation)

    def tourner(self, direction):
        if direction == 'G':
            new_orientation = Direction.tourner_a_gauche(self._orientation)
        elif direction == 'D':
            new_orientation = Direction.tourner_a_droite(self._orientation)
        else:
            raise ValueError(f"Direction invalide : {direction}")
        return EtatRover(self._position, new_orientation)

    def get_position(self):
        x, y = self._position.get_coords()
        return x, y, self._orientation.name

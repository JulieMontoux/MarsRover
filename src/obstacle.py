from abc import ABC, abstractmethod

# Interface pour les obstacles.
class ObstacleBase(ABC):
    @abstractmethod
    def detecter(self, position):
        pass

# Représente des obstacles fixes sur une planète.
class ObstacleFixe(ObstacleBase):
    def __init__(self, positions):
        self.positions = set(positions)

    def detecter(self, position):
        x, y = position.get_coords()
        if (x, y) in self.positions:
            return f"Obstacle détecté en ({x}, {y}) !"
        return f"Pas d'obstacle à la position ({x}, {y})."

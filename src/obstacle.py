# Représente une entité métier gérant les positions des obstacles sur la planète.
# Cette classe offre un service pour détecter si une position donnée est occupée.
class Obstacle:
    def __init__(self, positions):
        self.positions = set(positions)

    def detecter(self, position):
        x, y = position.get_coords()
        if (x, y) in self.positions:
            return f"Obstacle détecté en ({x}, {y}) !"
        return f"Pas d'obstacle à la position ({x}, {y})."
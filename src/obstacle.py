class Obstacle:
    def __init__(self, positions):
        self.positions = set(positions)

    def detecter(self, position):
        x, y = position.get_coords()
        if (x, y) in self.positions:
            return f"Obstacle détecté en ({x}, {y})."
        return f"Pas d'obstacle à la position ({x}, {y})."
    
    # fct pour prédire si c'est libre ou non return bool
from .position import Position
from .obstacle import Obstacle
from .direction import Direction

class Rover:
    def __init__(self, x, y, orientation, planete, obstacles=None):
        self.position = Position(x, y)
        self.orientation = Direction[orientation]
        self.planete = planete
        self.obstacles = Obstacle(obstacles if obstacles else [])

    def deplacer(self, mouvement):
        dx, dy = 0, 0
        if self.orientation == Direction.N:
            dy = 1 if mouvement == 'A' else -1
        elif self.orientation == Direction.S:
            dy = -1 if mouvement == 'A' else 1
        elif self.orientation == Direction.E:
            dx = -1 if mouvement == 'A' else 1
        elif self.orientation == Direction.W:
            dx = 1 if mouvement == 'A' else -1

        nouvelle_position = Position(
        (self.position.x + dx) % self.planete[0],
        (self.position.y + dy) % self.planete[1]
    )
        if self.obstacles.detecter(nouvelle_position).startswith("Obstacle détecté"):
            print(f"Impossible de se déplacer : obstacle détecté en {nouvelle_position.get_coords()}")
            return        
        self.position.deplacer(dx, dy, self.planete)

    def tourner(self, direction):
        if direction == 'G':
            self.orientation = Direction.tourner_a_gauche(self.orientation)
        elif direction == 'D':
            self.orientation = Direction.tourner_a_droite(self.orientation)

    def executer_commandes(self, commandes):
        for commande in commandes:
            if commande in ['A', 'R']:
                self.deplacer(commande)
            elif commande in ['G', 'D']:
                self.tourner(commande)
            else:
                print(f"Commande invalide : {commande}")

    def get_position(self):
        x, y = self.position.get_coords()
        return f"Position: ({x}, {y}), Orientation: {self.orientation.name}"

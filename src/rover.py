from src.etat_rover import EtatRover
from src.obstacle import ObstacleFixe
from src.position import Position
from src.direction import Direction

# Sert d'orchestrateur principal pour les interactions avec le rover.
# Cette classe délègue les responsabilités spécifiques à EtatRover (déplacement, rotation) et Obstacle (détection), tout en exposant une interface utilisateur claire.
class Rover:
    def __init__(self, x, y, orientation, planete, obstacles=None):
        self.etat = EtatRover(Position(x, y), Direction[orientation])
        self.planete = planete
        self.obstacles = ObstacleFixe(obstacles if obstacles else [])

    def deplacer(self, mouvement):
        nouvel_etat = self.etat.deplacer(mouvement, self.planete)
        detection = self.obstacles.detecter(nouvel_etat._position)
        if "Obstacle détecté" in detection:
            print(detection)
            return
        self.etat = nouvel_etat

    def tourner(self, direction):
        self.etat = self.etat.tourner(direction)

    def executer_commandes(self, commandes):
        for commande in commandes:
            if commande in ['A', 'R']:
                self.deplacer(commande)
            elif commande in ['G', 'D']:
                self.tourner(commande)
            else:
                print(f"Commande invalide : {commande}")

    def get_position(self):
        x, y, orientation = self.etat.get_position()
        return f"Position: ({x}, {y}), Orientation: {orientation}"
from .etat_rover import EtatRover
from .obstacle import Obstacle

# Sert d'orchestrateur principal pour les interactions avec le rover.
# Cette classe délègue les responsabilités spécifiques à EtatRover (déplacement, rotation) et Obstacle (détection), tout en exposant une interface utilisateur claire.
class Rover:
    def __init__(self, x, y, orientation, planete, obstacles=None):
        self.etat = EtatRover(x, y, orientation)
        self.planete = planete
        self.obstacles = Obstacle(obstacles if obstacles else [])

    def deplacer(self, mouvement):
        self.etat.deplacer(mouvement, self.planete)
        _x, _y = self.etat.position.get_coords()
        print(self.obstacles.detecter(self.etat.position))

    def tourner(self, direction):
        self.etat.tourner(direction)
    
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

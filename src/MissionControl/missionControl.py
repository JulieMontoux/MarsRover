from Rover.rover import Rover

class MissionControl:
    def __init__(self, planete, obstacles):
        self.rover = Rover(0, 0, 'N', planete, obstacles)

    def executer_commande(self, commande):
        if commande in ['A', 'R']:
            return self.rover.deplacer(commande)
        elif commande in ['G', 'D']:
            self.rover.tourner(commande)
            return "Rotation effectuée."
        return "Commande invalide."

    def get_position(self):
        return self.rover.get_position()

    def afficher_carte(self):
        self.rover.afficher_carte()

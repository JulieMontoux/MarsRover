from .etat_rover import EtatRover
from .direction import Direction

class Rover:
    def __init__(self, x, y, orientation, planete):
        self.position = EtatRover(x, y, Direction[orientation])
        self.planete = planete

    def avancer(self):
        self.position.avancer(self.planete)

    def reculer(self):
        self.position.reculer(self.planete)

    def tourner_a_gauche(self):
        self.position.tourner_a_gauche()

    def tourner_a_droite(self):
        self.position.tourner_a_droite()

    def get_position(self):
        return self.position.get_position()

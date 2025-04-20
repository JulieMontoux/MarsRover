from Rover.etat_rover import EtatRover
from Geometrie.position import Position
from Geometrie.direction import Direction
from obstacle.obstacle import ObstacleFixe

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
            return detection
        self.etat = nouvel_etat
        return "Déplacement effectué avec succès."

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

    def afficher_carte(self):
        x_rover, y_rover, _ = self.etat.get_position()
        grille = [['.' for _ in range(self.planete[0])] for _ in range(self.planete[1])]
        for ox, oy in self.obstacles.positions:
            grille[oy][ox] = 'X'
        grille[y_rover][x_rover] = 'R'
        print("\n=== Carte de Mars ===")
        for row in reversed(grille):
            print(" ".join(row))
        print("=====================\n")


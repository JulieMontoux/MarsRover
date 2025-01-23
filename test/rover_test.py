import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from src.rover import Rover
from src.etat_rover import EtatRover
from src.direction import Direction

class TestRover(unittest.TestCase):
    def setUp(self):
        # Création d'une planète 5x5 et initialisation du rover
        self.planete = (5, 5)
        self.rover = Rover(2, 2, 'N', self.planete)

    def test_initial_position(self):
        """Test de la position initiale du rover"""
        self.assertEqual(self.rover.get_position(), "Position: (2, 2), Orientation: N")

    def test_avancer(self):
        """Test du déplacement vers l'avant"""
        self.rover.avancer()
        self.assertEqual(self.rover.get_position(), "Position: (2, 1), Orientation: N")

    def test_avancer_bordure(self):
        """Test du déplacement qui dépasse les limites (rebouclage)"""
        self.rover.position = EtatRover(2, 0, Direction.N)
        self.rover.avancer()
        self.assertEqual(self.rover.get_position(), "Position: (2, 4), Orientation: N")

    def test_reculer(self):
        """Test du déplacement en arrière"""
        self.rover.reculer()
        self.assertEqual(self.rover.get_position(), "Position: (2, 3), Orientation: N")

    def test_reculer_bordure(self):
        """Test du recul avec rebouclage à la bordure"""
        self.rover.position = EtatRover(2, 4, Direction.N)
        self.rover.reculer()
        self.assertEqual(self.rover.get_position(), "Position: (2, 0), Orientation: N")

    def test_tourner_a_gauche(self):
        """Test de rotation à gauche"""
        self.rover.tourner_a_gauche()
        self.assertEqual(self.rover.get_position(), "Position: (2, 2), Orientation: W")
        self.rover.tourner_a_gauche()
        self.assertEqual(self.rover.get_position(), "Position: (2, 2), Orientation: S")

    def test_tourner_a_droite(self):
        """Test de rotation à droite"""
        self.rover.tourner_a_droite()
        self.assertEqual(self.rover.get_position(), "Position: (2, 2), Orientation: E")
        self.rover.tourner_a_droite()
        self.assertEqual(self.rover.get_position(), "Position: (2, 2), Orientation: S")

    def test_rotation_complete(self):
        """Test des rotations complètes (boucle sur les orientations)"""
        for _ in range(4):
            self.rover.tourner_a_gauche()
        self.assertEqual(self.rover.get_position(), "Position: (2, 2), Orientation: N")

        for _ in range(4):
            self.rover.tourner_a_droite()
        self.assertEqual(self.rover.get_position(), "Position: (2, 2), Orientation: N")

    def test_deplacement_et_rotation(self):
        """Test combiné de déplacement et de rotation"""
        self.rover.tourner_a_droite()  # Vers l'Est
        self.rover.avancer()  # Avance vers l'Est
        self.assertEqual(self.rover.get_position(), "Position: (3, 2), Orientation: E")

        self.rover.tourner_a_gauche()  # Vers le Nord
        self.rover.avancer()  # Avance vers le Nord
        self.assertEqual(self.rover.get_position(), "Position: (3, 1), Orientation: N")

    def test_deplacement_hors_grille(self):
        """Test des déplacements en dehors de la grille (rebouclage)"""
        self.rover.position = EtatRover(0, 0, Direction.W)  # Bord gauche
        self.rover.avancer()  # Se déplace vers la gauche
        self.assertEqual(self.rover.get_position(), "Position: (4, 0), Orientation: W")

        self.rover.position = EtatRover(4, 4, Direction.E)  # Bord droit
        self.rover.avancer()  # Se déplace vers la droite
        self.assertEqual(self.rover.get_position(), "Position: (0, 4), Orientation: E")


if __name__ == '__main__':
    unittest.main()
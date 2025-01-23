import unittest
import sys
import os

# Ajouter src au chemin des modules Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.rover import Rover

class TestRover(unittest.TestCase):

    def setUp(self):
        self.planete = (5, 5)
        self.rover = Rover(0, 0, 'N', self.planete)

    def test_initial_position(self):
        self.assertEqual(self.rover.get_position(), "Position: (0, 0), Orientation: N")

    def test_avancer_nord(self):
        self.rover.avancer()
        self.assertEqual(self.rover.get_position(), "Position: (0, 4), Orientation: N")

    def test_reculer_nord(self):
        self.rover.reculer()
        self.assertEqual(self.rover.get_position(), "Position: (0, 1), Orientation: N")

    def test_tourner_a_gauche(self):
        self.rover.tourner_a_gauche()
        self.assertEqual(self.rover.get_position(), "Position: (0, 0), Orientation: W")

    def test_tourner_a_droite(self):
        self.rover.tourner_a_droite()
        self.assertEqual(self.rover.get_position(), "Position: (0, 0), Orientation: E")

    def test_avancer_est(self):
        self.rover.tourner_a_droite()
        self.rover.avancer()
        self.assertEqual(self.rover.get_position(), "Position: (1, 0), Orientation: E")

    def test_reculer_ouest(self):
        self.rover.tourner_a_gauche()
        self.rover.reculer()
        self.assertEqual(self.rover.get_position(), "Position: (1, 0), Orientation: W")

    def test_deplacement_circulaire(self):
        self.rover.avancer()
        self.rover.tourner_a_droite()
        self.rover.avancer()
        self.assertEqual(self.rover.get_position(), "Position: (1, 4), Orientation: E")

    def test_bouclage_planete(self):
        self.rover.avancer()
        self.rover.avancer()
        self.rover.avancer()
        self.rover.avancer()
        self.rover.avancer()
        self.assertEqual(self.rover.get_position(), "Position: (0, 0), Orientation: N")

if __name__ == '__main__':
    unittest.main()

import unittest
import sys
import os
from src.rover import Rover

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
class TestRover(unittest.TestCase):

    def setUp(self):
        self.planete = (5, 5)
        self.rover = Rover(0, 0, 'N', self.planete)

    def test_initial_position(self):
        self.assertEqual(self.rover.get_position(), "Position: (0, 0), Orientation: N")

    def test_avancer_nord(self):
        self.rover.deplacer("A")
        self.assertEqual(self.rover.get_position(), "Position: (0, 4), Orientation: N")

    def test_reculer_nord(self):
        self.rover.deplacer("R")
        self.assertEqual(self.rover.get_position(), "Position: (0, 1), Orientation: N")

    def test_tourner_a_gauche(self):
        self.rover.tourner("G")
        self.assertEqual(self.rover.get_position(), "Position: (0, 0), Orientation: W")

    def test_tourner_a_droite(self):
        self.rover.tourner("D")
        self.assertEqual(self.rover.get_position(), "Position: (0, 0), Orientation: E")

    def test_avancer_est(self):
        self.rover.tourner("D")
        self.rover.deplacer("A")
        self.assertEqual(self.rover.get_position(), "Position: (1, 0), Orientation: E")

    def test_reculer_ouest(self):
        self.rover.tourner("G")
        self.rover.deplacer("R")
        self.assertEqual(self.rover.get_position(), "Position: (1, 0), Orientation: W")

    def test_deplacement_circulaire(self):
        self.rover.deplacer("A")
        self.rover.tourner("G")
        self.rover.deplacer("R")
        self.assertEqual(self.rover.get_position(), "Position: (1, 4), Orientation: W")

    def test_bouclage_planete(self):
        self.rover.deplacer("R")
        self.rover.deplacer("R")
        self.rover.deplacer("R")
        self.rover.deplacer("R")
        self.rover.deplacer("R")
        self.assertEqual(self.rover.get_position(), "Position: (0, 0), Orientation: N")

    def test_rover_avancer(self):
        planete = (10, 10)
        rover = Rover(5, 5, 'N', planete)
        rover.deplacer('A')
        self.assertEqual(rover.get_position(), "Position: (5, 4), Orientation: N")

    def test_rover_reculer(self):
        planete = (10, 10)
        rover = Rover(5, 5, 'N', planete)
        rover.deplacer('R')
        self.assertEqual(rover.get_position(), "Position: (5, 6), Orientation: N")

    def test_rover_tourner(self):
        planete = (10, 10)
        rover = Rover(5, 5, 'N', planete)
        rover.tourner('G')
        self.assertEqual(rover.get_position(), "Position: (5, 5), Orientation: W")

    def test_rover_obstacle(self):
        planete = (10, 10)
        obstacles = [(5, 4)]
        rover = Rover(5, 5, 'N', planete, obstacles)
        detection_message = rover.deplacer('A')
        self.assertIn("Obstacle détecté", detection_message)
        self.assertEqual(rover.get_position(), "Position: (5, 5), Orientation: N")

if __name__ == '__main__':
    unittest.main()
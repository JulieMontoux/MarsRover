import unittest
from rover import Rover
from etat_rover import EtatRover
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestRover(unittest.TestCase):
    def setUp(self):
        self.planete = (5, 5)
        self.rover = Rover(2, 2, 'N', self.planete)

    def test_initial_position(self):
        self.assertEqual(self.rover.get_position(), "Position: (2, 2), Orientation: N")

    def test_avancer(self):
        self.rover.avancer()
        self.assertEqual(self.rover.get_position(), "Position: (2, 1), Orientation: N")

    def test_avancer_bordure(self):
        self.rover.position = EtatRover(2, 0, 'N')
        self.rover.avancer()
        self.assertEqual(self.rover.get_position(), "Position: (2, 4), Orientation: N")  

    def test_reculer(self):
        self.rover.reculer()
        self.assertEqual(self.rover.get_position(), "Position: (2, 3), Orientation: N")

    def test_reculer_bordure(self):
        self.rover.position = EtatRover(2, 4, 'N')
        self.rover.reculer()
        self.assertEqual(self.rover.get_position(), "Position: (2, 0), Orientation: N")  

    def test_tourner_a_gauche(self):
        self.rover.tourner_a_gauche()
        self.assertEqual(self.rover.get_position(), "Position: (2, 2), Orientation: W")
        self.rover.tourner_a_gauche()
        self.assertEqual(self.rover.get_position(), "Position: (2, 2), Orientation: S")

    def test_tourner_a_droite(self):
        self.rover.tourner_a_droite()
        self.assertEqual(self.rover.get_position(), "Position: (2, 2), Orientation: E")
        self.rover.tourner_a_droite()
        self.assertEqual(self.rover.get_position(), "Position: (2, 2), Orientation: S")

    def test_boucle_orientations(self):
        self.rover.tourner_a_gauche()
        self.rover.tourner_a_gauche()
        self.rover.tourner_a_gauche()
        self.rover.tourner_a_gauche()
        self.assertEqual(self.rover.get_position(), "Position: (2, 2), Orientation: N")

        self.rover.tourner_a_droite()
        self.rover.tourner_a_droite()
        self.rover.tourner_a_droite()
        self.rover.tourner_a_droite()
        self.assertEqual(self.rover.get_position(), "Position: (2, 2), Orientation: N")

    def test_mouvement_et_rotation(self):
        self.rover.tourner_a_droite()
        self.rover.avancer()
        self.assertEqual(self.rover.get_position(), "Position: (3, 2), Orientation: E")

        self.rover.tourner_a_gauche()
        self.rover.avancer()
        self.assertEqual(self.rover.get_position(), "Position: (3, 1), Orientation: N")

    def test_deplacement_hors_grille(self):
        self.rover.position = EtatRover(0, 0, 'W')
        self.rover.avancer()
        self.assertEqual(self.rover.get_position(), "Position: (4, 0), Orientation: W")  

        self.rover.position = EtatRover(4, 4, 'E')
        self.rover.avancer()
        self.assertEqual(self.rover.get_position(), "Position: (0, 4), Orientation: E")  

if __name__ == '__main__':
    unittest.main()

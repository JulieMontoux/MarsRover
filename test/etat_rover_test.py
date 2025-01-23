import unittest
from etat_rover import EtatRover

class TestEtatRover(unittest.TestCase):
    def test_deplacer_avancer(self):
        planete = (10, 10)
        etat = EtatRover(5, 5, 'N')
        etat.deplacer('A', planete)
        self.assertEqual(etat.get_position(), (5, 4, 'N'))

    def test_deplacer_reculer(self):
        planete = (10, 10)
        etat = EtatRover(5, 5, 'N')
        etat.deplacer('R', planete)
        self.assertEqual(etat.get_position(), (5, 6, 'N'))

    def test_tourner(self):
        etat = EtatRover(5, 5, 'N')
        etat.tourner('G')
        self.assertEqual(etat.get_position(), (5, 5, 'W'))
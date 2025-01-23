import unittest
from src.etat_rover import EtatRover
from src.position import Position
from src.direction import Direction

class TestEtatRover(unittest.TestCase):
    def test_deplacer_avancer(self):
        planete = (10, 10)
        etat = EtatRover(Position(5, 5), Direction.N)
        nouvel_etat = etat.deplacer('A', planete)
        self.assertEqual(nouvel_etat.get_position(), (5, 4, 'N'))

    def test_deplacer_reculer(self):
        planete = (10, 10)
        etat = EtatRover(Position(5, 5), Direction.N)
        nouvel_etat = etat.deplacer('R', planete)
        self.assertEqual(nouvel_etat.get_position(), (5, 6, 'N'))

    def test_tourner(self):
        etat = EtatRover(Position(5, 5), Direction.N)
        nouvel_etat = etat.tourner('G')
        self.assertEqual(nouvel_etat.get_position(), (5, 5, 'W'))

if __name__ == "__main__":
    unittest.main()

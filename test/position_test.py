import unittest
from position import Position

class TestPosition(unittest.TestCase):
    def test_deplacer_simple(self):
        planete = (10, 10)
        pos = Position(5, 5)
        pos.deplacer(1, 0, planete)
        self.assertEqual(pos.get_coords(), (6, 5))

    def test_deplacer_toroidal(self):
        planete = (10, 10)
        pos = Position(9, 9)
        pos.deplacer(1, 0, planete)
        self.assertEqual(pos.get_coords(), (0, 9))
import unittest
from Rover.position import Position

class TestPosition(unittest.TestCase):
    def test_deplacer_simple(self):
        planete = (10, 10)
        pos = Position(5, 5)
        new_pos = pos.deplacer(1, 0, planete)
        self.assertEqual(new_pos.get_coords(), (6, 5))

    def test_deplacer_toroidal(self):
        planete = (10, 10)
        pos = Position(9, 9)
        new_pos = pos.deplacer(1, 0, planete)
        self.assertEqual(new_pos.get_coords(), (0, 9))

    def test_get_coords(self):
        pos = Position(3, 4)
        self.assertEqual(pos.get_coords(), (3, 4))

if __name__ == "__main__":
    unittest.main()
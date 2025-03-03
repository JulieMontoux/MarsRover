import unittest
from src.MissionControl.direction import Direction

class TestDirection(unittest.TestCase):

    def test_tourner_a_gauche(self):
        self.assertEqual(Direction.tourner_a_gauche(Direction.N), Direction.W)
        self.assertEqual(Direction.tourner_a_gauche(Direction.E), Direction.N)

    def test_tourner_a_droite(self):
        self.assertEqual(Direction.tourner_a_droite(Direction.N), Direction.E)
        self.assertEqual(Direction.tourner_a_droite(Direction.W), Direction.N)

    def test_get_delta(self):
        self.assertEqual(Direction.get_delta(Direction.N), (0, -1))
        self.assertEqual(Direction.get_delta(Direction.S), (0, 1))
        self.assertEqual(Direction.get_delta(Direction.E), (1, 0))
        self.assertEqual(Direction.get_delta(Direction.W), (-1, 0))

if __name__ == "__main__":
    unittest.main()
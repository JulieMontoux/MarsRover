import unittest
from obstacle import Obstacle
from position import Position

class TestObstacle(unittest.TestCase):
    def test_detection_obstacle(self):
        obstacles = Obstacle([(3, 3), (5, 5)])
        pos1 = Position(3, 3)
        pos2 = Position(1, 1)
        self.assertIn("Obstacle détecté", obstacles.detecter(pos1))
        self.assertIn("Pas d'obstacle", obstacles.detecter(pos2))
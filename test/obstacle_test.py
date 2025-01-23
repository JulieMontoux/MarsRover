import unittest
from src.obstacle import ObstacleFixe
from src.position import Position

class TestObstacleFixe(unittest.TestCase):
    def test_detection_obstacle(self):
        obstacles = ObstacleFixe([(3, 3), (5, 5)])
        pos1 = Position(3, 3)
        pos2 = Position(1, 1)
        self.assertIn("Obstacle détecté", obstacles.detecter(pos1))
        self.assertIn("Pas d'obstacle", obstacles.detecter(pos2))

if __name__ == "__main__":
    unittest.main()

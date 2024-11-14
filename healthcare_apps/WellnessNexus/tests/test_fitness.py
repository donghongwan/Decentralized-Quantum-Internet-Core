import unittest
from models.fitness import Fitness

class TestFitness(unittest.TestCase):
    def test_fitness_creation(self):
        fitness = Fitness("Running", 30, 300)
        self.assertEqual(fitness.activity, "Running")
        self.assertEqual(fitness.duration, 30)
        self.assertEqual(fitness.calories_burned, 300)

if __name__ == '__main__':
    unittest.main()

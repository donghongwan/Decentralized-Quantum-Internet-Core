import unittest
from models.mental_health import MentalHealth

class TestMentalHealth(unittest.TestCase):
    def test_mental_health_creation(self):
        mental_health = MentalHealth("Happy", "Feeling great today!", "2023-10-01")
        self.assertEqual(mental_health.mood, "Happy")
        self.assertEqual(mental_health.notes, "Feeling great today!")
        self.assertEqual(mental_health.date, "2023-10-01")

if __name__ == '__main__':
    unittest.main()

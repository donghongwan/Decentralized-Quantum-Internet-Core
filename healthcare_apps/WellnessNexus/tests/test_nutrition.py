import unittest
from models.nutrition import Nutrition

class TestNutrition(unittest.TestCase):
    def test_nutrition_creation(self):
        nutrition = Nutrition("Breakfast", 400, "2023-10-01")
        self.assertEqual(nutrition.meal, "Breakfast")
        self.assertEqual(nutrition.calories, 400)
        self.assertEqual(nutrition.date, "2023-10-01")

if __name__ == '__main__':
    unittest.main()

import unittest
from models.budget import Budget

class TestBudget(unittest.TestCase):
    def test_budget_creation(self):
        budget = Budget("Food", 500)
        self.assertEqual(budget.category, "Food")
        self.assertEqual(budget.limit, 500)

if __name__ == '__main__':
    unittest.main()

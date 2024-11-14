import unittest
from models.transaction import Transaction

class TestTransaction(unittest.TestCase):
    def test_transaction_creation(self):
        transaction = Transaction(100, "Groceries", "2023-10-01")
        self.assertEqual(transaction.amount, 100)
        self.assertEqual(transaction.category, "Groceries")
        self.assertEqual(transaction.date, "2023-10-01")

if __name__ == '__main__':
    unittest.main()

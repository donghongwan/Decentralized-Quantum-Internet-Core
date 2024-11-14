import unittest
from examples.finance_app.app import FinanceApp

class TestFinanceAppIntegration(unittest.TestCase):
    def setUp(self):
        self.app = FinanceApp()

    def test_send_receive_transaction(self):
        transaction = '{"amount": 1000, "to": "AccountB"}'
        self.app.send_transaction(transaction)
        self.app.receive_transaction()

        # Here you would assert the expected outcome
        # For example, check if the received transaction matches the sent one
        self.assertEqual(self.app.node_b.state, self.app.node_a.encrypt(transaction))

if __name__ == "__main__":
    unittest.main()

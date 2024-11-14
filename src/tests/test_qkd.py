import unittest
from src.core.quantum_comm import QuantumComm
from src.core.qkd import QKD

class TestQKD(unittest.TestCase):
    def setUp(self):
        self.node_a = QuantumComm(node_id="A")
        self.node_b = QuantumComm(node_id="B")
        self.qkd = QKD(sender=self.node_a, receiver=self.node_b)

    def test_generate_key(self):
        """Test key generation."""
        self.qkd.generate_key(length=5)
        self.assertEqual(len(self.qkd.key), 5)  # Check if the key length is correct

    def test_exchange_key(self):
        """Test key exchange."""
        self.qkd.generate_key(length=5)
        self.qkd.exchange_key()
        self.assertIsNotNone(self.qkd.key)  # Ensure the key is not None after exchange

if __name__ == "__main__":
    unittest.main()

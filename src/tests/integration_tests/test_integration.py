# Placeholder for integration tests
# Example: test_integration.py

import unittest
from src.core.quantum_comm import QuantumComm
from src.core.qkd import QKD
from src.core.entanglement import Entanglement

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.node_a = QuantumComm(node_id="A")
        self.node_b = QuantumComm(node_id="B")
        self.qkd = QKD(sender=self.node_a, receiver=self.node_b)
        self.entanglement = Entanglement()

    def test_qkd_with_entanglement(self):
        """Test QKD using entangled states."""
        state_a, state_b = self.entanglement.create_entangled_pair()
        self.node_a.send(state_a, self.node_b)
        self.qkd.generate_key(length=5)
        self.qkd.exchange_key()
        self.assertIsNotNone(self.qkd.key)

if __name__ == "__main__":
    unittest.main()

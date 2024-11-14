import unittest
from src.core.entanglement import Entanglement

class TestEntanglement(unittest.TestCase):
    def setUp(self):
        self.entanglement = Entanglement()

    def test_create_entangled_pair(self):
        """Test creating an entangled pair."""
        state_a, state_b = self.entanglement.create_entangled_pair()
        self.assertIsNotNone(state_a)
        self.assertIsNotNone(state_b)
        self.assertEqual(len(state_a), 4)  # Check the length of the Bell state

    def test_measurement(self):
        """Test measurement of a quantum state."""
        state = self.entanglement.create_entangled_pair()[0]
        measurement_result = self.entanglement.measure(state)
        self.assertIn(measurement_result, [0, 1])  # Measurement should be 0 or 1

if __name__ == "__main__":
    unittest.main()

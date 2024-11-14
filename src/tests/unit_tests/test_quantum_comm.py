import unittest
from src.core.quantum_comm import QuantumComm

class TestQuantumComm(unittest.TestCase):
    def setUp(self):
        self.node_a = QuantumComm(node_id="A")
        self.node_b = QuantumComm(node_id="B")

    def test_send_receive_message(self):
        """Test sending and receiving a message."""
        message = "Hello, Quantum World!"
        self.node_a.send(message, self.node_b)
        self.assertEqual(self.node_b.decode_message(self.node_b.state), message)

    def test_encode_decode_message(self):
        """Test encoding and decoding a message."""
        message = "Test Message"
        encoded = self.node_a.encode_message(message)
        decoded = self.node_a.decode_message(encoded)
        self.assertEqual(decoded, message)

if __name__ == "__main__":
    unittest.main()

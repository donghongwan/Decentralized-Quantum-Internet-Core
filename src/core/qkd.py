import numpy as np
from quantum_comm import QuantumComm

class QKD:
    def __init__(self, sender: QuantumComm, receiver: QuantumComm):
        self.sender = sender
        self.receiver = receiver
        self.key = []

    def generate_key(self, length=10):
        """Generate a quantum key using BB84 protocol."""
        for _ in range(length):
            bit = np.random.randint(0, 2)
            self.key.append(bit)
            self.sender.send(bit, self.receiver)

    def exchange_key(self):
        """Exchange keys and perform basis reconciliation."""
        print(f"Key exchanged between {self.sender.node_id} and {self.receiver.node_id}: {self.key}")

# Example usage
if __name__ == "__main__":
    node_a = QuantumComm(node_id="A")
    node_b = QuantumComm(node_id="B")
    qkd = QKD(sender=node_a, receiver=node_b)
    qkd.generate_key()
    qkd.exchange_key()

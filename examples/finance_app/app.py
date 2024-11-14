from src.core.quantum_comm import QuantumComm
from src.core.qkd import QKD
import json

class FinanceApp:
    def __init__(self):
        self.node_a = QuantumComm(node_id="FinanceNodeA")
        self.node_b = QuantumComm(node_id="FinanceNodeB")
        self.qkd = QKD(sender=self.node_a, receiver=self.node_b)

    def send_transaction(self, transaction):
        """Send a secure transaction."""
        self.qkd.generate_key(length=16)
        encrypted_transaction = self.node_a.encrypt(transaction)
        self.node_a.send(encrypted_transaction, self.node_b)
        print("Transaction sent securely.")

    def receive_transaction(self):
        """Receive a secure transaction."""
        encrypted_transaction = self.node_b.state
        decrypted_transaction = self.node_b.decrypt(encrypted_transaction)
        print("Received transaction:", decrypted_transaction)

if __name__ == "__main__":
    app = FinanceApp()
    transaction = json.dumps({"amount": 1000, "to": "AccountB"})
    app.send_transaction(transaction)
    app.receive_transaction()

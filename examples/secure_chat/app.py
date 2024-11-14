from src.core.quantum_comm import QuantumComm
from src.core.qkd import QKD

class SecureChat:
    def __init__(self):
        self.node_a = QuantumComm(node_id="ChatNodeA")
        self.node_b = QuantumComm(node_id="ChatNodeB")
        self.qkd = QKD(sender=self.node_a, receiver=self.node_b)

    def send_message(self, message):
        """Send a secure chat message."""
        self.qkd.generate_key(length=16)
        encrypted_message = self.node_a.encrypt(message)
        self.node_a.send(encrypted_message, self.node_b)
        print("Message sent securely.")

    def receive_message(self):
        """Receive a secure chat message."""
        encrypted_message = self.node_b.state
        decrypted_message = self.node_b.decrypt(encrypted_message)
        print("Received message:", decrypted_message)

if __name__ == "__main__":
    chat = SecureChat()
    chat.send_message("Hello, this is a secure message!")
    chat.receive_message()

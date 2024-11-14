from src.core.quantum_comm import QuantumComm
from src.core.qkd import QKD
import json

class VotingSystem:
    def __init__(self):
        self.node_a = QuantumComm(node_id="VotingNodeA")
        self.node_b = QuantumComm(node_id="VotingNodeB")
        self.qkd = QKD(sender=self.node_a, receiver=self.node_b)

    def cast_vote(self, vote):
        """Cast a secure vote."""
        self.qkd.generate_key(length=16)
        encrypted_vote = self.node_a.encrypt(vote)
        self.node_a.send(encrypted_vote, self.node_b)
        print("Vote cast securely.")

    def receive_vote(self):
        """Receive a secure vote."""
        encrypted_vote = self.node_b.state
        decrypted_vote = self.node_b.decrypt(encrypted_vote)
        print("Received vote:", decrypted_vote)

if __name__ == "__main__":
    voting_app = VotingSystem()
    vote = json.dumps({"candidate": "Candidate A"})
    voting_app.cast_vote(vote)
    voting_app.receive_vote()

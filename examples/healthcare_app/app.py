from src.core.quantum_comm import QuantumComm
from src.core.qkd import QKD
import json

class HealthcareApp:
    def __init__(self):
        self.node_a = QuantumComm(node_id="HealthcareNodeA")
        self.node_b = QuantumComm(node_id="HealthcareNodeB")
        self.qkd = QKD(sender=self.node_a, receiver=self.node_b)

    def send_patient_data(self, patient_data):
        """Send secure patient data."""
        self.qkd.generate_key(length=32)
        encrypted_data = self.node_a.encrypt(json.dumps(patient_data))
        self.node_a.send(encrypted_data, self.node_b)
        print("Patient data sent securely.")

    def receive_patient_data(self):
        """Receive secure patient data."""
        encrypted_data = self.node_b.state
        decrypted_data = self.node_b.decrypt(encrypted_data)
        print("Received patient data:", decrypted_data)

if __name__ == "__main__":
    app = HealthcareApp()
    patient_data = {"name": "John Doe", "age": 30, "condition": "Healthy"}
    app.send_patient_data(patient_data)
    app.receive_patient_data()

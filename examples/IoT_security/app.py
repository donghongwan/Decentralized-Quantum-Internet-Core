from src.core.quantum_comm import QuantumComm
from src.core.qkd import QKD
import json

class IoTSecurity:
    def __init__(self):
        self.node_a = QuantumComm(node_id="IoTNodeA")
        self.node_b = QuantumComm(node_id="IoTNodeB")
        self.qkd = QKD(sender=self.node_a, receiver=self.node_b)

    def secure_device_data(self, device_data):
        """Send secure data from IoT device."""
        self.qkd.generate_key(length=32)
        encrypted_data = self.node_a.encrypt(json.dumps(device_data))
        self.node_a.send(encrypted_data, self.node_b)
        print("Device data sent securely.")

    def receive_device_data(self):
        """Receive secure data from IoT device."""
        encrypted_data = self.node_b.state
        decrypted_data = self.node_b.decrypt(encrypted_data)
        print("Received device data:", decrypted_data)

if __name__ == "__main__":
    iot_app = IoTSecurity()
    device_data = {"temperature": 22.5, "humidity": 60}
    iot_app.secure_device_data(device_data)
    iot_app.receive_device_data()

import unittest
from examples.IoT_security.app import IoTSecurity

class TestIoTSecurityIntegration(unittest.TestCase):
    def setUp(self):
        self.iot_app = IoTSecurity()

    def test_secure_device_data(self):
        device_data = {"temperature": 22.5, "humidity": 60}
        self.iot_app.secure_device_data(device_data)
        self.iot_app.receive_device_data()

        # Assert that the received data matches the sent data
        self.assertEqual(self.iot_app.node_b.state, self.iot_app.node_a.encrypt(str(device_data)))

if __name__ == "__main__":
    unittest.main()

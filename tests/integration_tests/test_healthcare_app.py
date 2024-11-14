import unittest
from examples.healthcare_app.app import HealthcareApp

class TestHealthcareAppIntegration(unittest.TestCase):
    def setUp(self):
        self.app = HealthcareApp()

    def test_send_receive_patient_data(self):
        patient_data = {"name": "John Doe", "age": 30, "condition": "Healthy"}
        self.app.send_patient_data(patient_data)
        self.app.receive_patient_data()

        # Assert that the received data matches the sent data
        self.assertEqual(self.app.node_b.state, self.app.node_a.encrypt(str(patient_data)))

if __name__ == "__main__":
    unittest.main()

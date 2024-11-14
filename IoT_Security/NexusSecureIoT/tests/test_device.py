import unittest
from models.device import Device

class TestDevice(unittest.TestCase):
    def test_device_initialization(self):
        device = Device("123", "sensor", "user@example.com")
        self.assertEqual(device.device_id, "123")
        self.assertEqual(device.device_type, "sensor")
        self.assertEqual(device.owner, "user@example.com")

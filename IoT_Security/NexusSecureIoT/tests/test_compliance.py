import unittest
from models.compliance import Compliance

class TestCompliance(unittest.TestCase):
    def test_compliance_initialization(self):
        compliance = Compliance("123", "compliant")
        self.assertEqual(compliance.device_id, "123")
        self.assertEqual(compliance.compliance_status, "compliant")

import unittest
from models.blockchain_record import BlockchainRecord

class TestBlockchainRecord(unittest.TestCase):
    def test_blockchain_record_initialization(self):
        record = BlockchainRecord("1", "123", "register", "2023-10-01T12:00:00Z")
        self.assertEqual(record.record_id, "1")
        self.assertEqual(record.device_id, "123")
        self.assertEqual(record.action, "register")

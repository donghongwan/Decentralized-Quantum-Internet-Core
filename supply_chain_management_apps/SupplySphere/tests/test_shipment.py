import unittest
from app import app, db
from models import Shipment

class ShipmentModelTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_shipment_creation(self):
        response = self.app.post('/shipments', json={
            'product_id': 1,
            'supplier_id': 1,
            'manufacturer_id': 1,
            'consumer_id': 1,
            'status': 'in transit'
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()

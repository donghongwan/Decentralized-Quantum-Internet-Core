import unittest
from app import app, db
from models import Inventory

class InventoryModelTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_inventory_addition(self):
        response = self.app.post('/inventory', json={
            'product_id': 1,
            'quantity': 100,
            'location': 'Warehouse A'
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()

import unittest
from main import app

class ProductTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_product(self):
        response = self.app.post('/product', json={
            'name': 'AR Glasses',
            'description': 'High-tech glasses for AR experiences.',
            'image': 'url_to_image',
            'price': 299.99,
            'stock': 50
        })
        self.assertEqual(response.status_code, 201)

import unittest
from main import app

class ResourceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_share_resource(self):
        response = self.app.post('/resources', json={'title': 'Test Resource', 'description': 'A resource for testing', 'owner_id': 1})
        self.assertEqual(response.status_code, 201)

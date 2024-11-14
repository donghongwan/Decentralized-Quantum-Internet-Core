import unittest
from main import app

class GroupTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_group(self):
        response = self.app.post('/groups', json={'name': 'Test Group', 'description': 'A group for testing'})
        self.assertEqual(response.status_code, 201)

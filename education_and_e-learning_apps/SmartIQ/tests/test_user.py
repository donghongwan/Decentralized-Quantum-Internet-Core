import unittest
from main import app

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_register(self):
        response = self.app.post('/register', json={'username': 'testuser', 'email': 'test@example.com', 'password': 'password'})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'User  registered successfully!', response.data)

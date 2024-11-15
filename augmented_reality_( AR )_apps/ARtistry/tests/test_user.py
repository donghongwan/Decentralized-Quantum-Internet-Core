import unittest
from main import app

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_register_user(self):
        response = self.app.post('/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'securepassword'
        })
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        self.app.post('/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'securepassword'
        })
        response = self.app.post('/login', json={
            'email': 'test@example.com',
            'password': 'securepassword'
        })
        self.assertEqual(response.status_code, 200)

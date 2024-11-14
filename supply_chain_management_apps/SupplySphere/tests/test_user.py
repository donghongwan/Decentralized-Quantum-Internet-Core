import unittest
from app import app, db
from models import User

class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_registration(self):
        response = self.app.post('/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password',
            'role': 'consumer'
        })
        self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        self.app.post('/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password',
            'role': 'consumer'
        })
        response = self.app.post('/login', json={
            'username': 'testuser',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

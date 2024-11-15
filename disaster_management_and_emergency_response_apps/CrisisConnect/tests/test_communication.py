import unittest
from app import app, db
from models.communication import Communication

class CommunicationModelTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_send_message(self):
        response = self.client.post('/messages', json={'user_id': 1, 'message': 'Help needed!'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

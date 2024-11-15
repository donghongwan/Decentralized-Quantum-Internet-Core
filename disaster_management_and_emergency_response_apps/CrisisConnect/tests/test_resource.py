import unittest
from app import app, db
from models.resource import Resource

class ResourceModelTest(unittest.TestCase):
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

    def test_add_resource(self):
        response = self.client.post('/resources', json={'type': 'Water', 'quantity': 100, 'location': 'Shelter', 'incident_id': 1})
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

import unittest
from app import app, db
from models.incident import Incident

class IncidentModelTest(unittest.TestCase):
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

    def test_create_incident(self):
        response = self.client.post('/incidents', json={'title': 'Flood', 'description': 'Severe flooding in the area', 'location': 'Downtown', 'status': 'Active'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

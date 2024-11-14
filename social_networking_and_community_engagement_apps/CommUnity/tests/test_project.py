import unittest
from main import app

class ProjectTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_project(self):
        response = self.app.post('/projects', json={'title': 'Test Project', 'description': 'A project for testing'})
        self.assertEqual(response.status_code, 201)

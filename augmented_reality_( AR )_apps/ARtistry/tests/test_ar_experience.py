import unittest
from main import app

class ARExperienceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_ar_experience(self):
        response = self.app.post('/experience', json={
            'title': 'Virtual Museum',
            'description': 'An immersive AR experience in a virtual museum.',
            'content': '3D models of historical artifacts.'
        })
        self.assertEqual(response.status_code, 201)

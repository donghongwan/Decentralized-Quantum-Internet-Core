import unittest
from main import app

class SoilTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_soil_moisture(self):
        response = self.app.get('/soil/1/moisture')
        self.assertEqual(response.status_code, 200)

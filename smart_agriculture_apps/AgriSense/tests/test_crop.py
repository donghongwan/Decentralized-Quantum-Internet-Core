import unittest
from main import app

class CropTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_crop_health(self):
        response = self.app.get('/crop/1/health')
        self.assertEqual(response.status_code, 200)

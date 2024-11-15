import unittest
from main import app

class ProgressTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_update_progress(self):
        response = self.app.post('/progress', json={'user_id': 1, 'course_id': 1, 'completion_percentage': 75.0})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Progress updated successfully!', response.data)

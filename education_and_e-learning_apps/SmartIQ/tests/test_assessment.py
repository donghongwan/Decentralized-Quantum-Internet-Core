import unittest
from main import app

class AssessmentTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_assessment(self):
        response = self.app.post('/assessments', json={'course_id': 1, 'questions': 'What is AI?', 'answers': 'Artificial Intelligence'})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Assessment created successfully!', response.data)

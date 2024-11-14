import unittest
from main import app

class EventTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_event(self):
        self.app.post('/groups', json={'name': 'Test Group', 'description': 'A group for testing'})
        response = self.app.post('/events', json={'title': 'Test Event', 'description': 'An event for testing', 'date': '2023-10-01T10:00:00', 'group_id': 1})
        self.assertEqual(response.status_code, 201)

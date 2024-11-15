import unittest
from main import app

class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_game_session(self):
        response = self.app.post('/session', json={
            'user_id': 1,
            'score': 100,
            'duration': 30.5
        })
        self.assertEqual(response.status_code, 201)

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_user_initialization(self):
        user = User("testuser", "test@example.com")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")

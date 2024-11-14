import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_add_contact(self):
        user = User("testuser", "test@example.com")
        user.add_contact("friend")
        self.assertIn("friend", user.contacts)

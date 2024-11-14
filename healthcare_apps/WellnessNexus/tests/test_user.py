import unittest
from models.user import User

class TestUser (unittest.TestCase):
    def test_user_creation(self):
        user = User("testuser", "test@example.com")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")

if __name__ == '__main__':
    unittest.main()

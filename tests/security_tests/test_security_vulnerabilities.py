import unittest
from examples.secure_chat.app import SecureChat

class TestSecurityVulnerabilities(unittest.TestCase):
    def setUp(self):
        self.chat = SecureChat()

    def test_message_encryption(self):
        message = "Sensitive information"
        encrypted_message = self.chat.node_a.encrypt(message)
        decrypted_message = self.chat.node_b.decrypt(encrypted_message)

        # Assert that the decrypted message matches the original message
        self.assertEqual(decrypted_message, message)

    def test_sql_injection(self):
        malicious_input = "'; DROP TABLE users; --"
        result = self.chat.handle_input(malicious_input)

        # Assert that the application handles the input safely
        self.assertNotIn("users", result)

if __name__ == "__main__":
    unittest.main()

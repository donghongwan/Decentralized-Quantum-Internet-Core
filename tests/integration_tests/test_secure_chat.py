import unittest
from examples.secure_chat.app import SecureChat

class TestSecureChatIntegration(unittest.TestCase):
    def setUp(self):
        self.chat = SecureChat()

    def test_send_receive_message(self):
        message = "Hello, this is a secure message!"
        self.chat.send_message(message)
        self.chat.receive_message()

        # Assert that the received message matches the sent message
        self.assertEqual(self.chat.node_b.state, self.chat.node_a.encrypt(message))

if __name__ == "__main__":
    unittest.main()

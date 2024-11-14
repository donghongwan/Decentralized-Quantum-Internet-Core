import unittest
from services.chat_service import ChatService

class TestChatService(unittest.TestCase):
    def test_send_message(self):
        chat_service = ChatService()
        result = chat_service.send_message("user1", "user2", "Hello")
        self.assertEqual(result, "Message sent successfully")

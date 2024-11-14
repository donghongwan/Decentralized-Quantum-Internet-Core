import time
import unittest
from examples.secure_chat.app import SecureChat

class TestPerformance(unittest.TestCase):
    def setUp(self):
        self.chat = SecureChat()

    def test_performance_message_sending(self):
        start_time = time.time()
        for _ in range(100):  # Send 100 messages
            self.chat.send_message("Performance test message")
            self.chat.receive_message()
        end_time = time.time()

        total_time = end_time - start_time
        print(f"Total time for 100 messages: {total_time:.2f} seconds")
        self.assertLess(total_time, 5)  # Example threshold

if __name__ == "__main__":
    unittest.main()

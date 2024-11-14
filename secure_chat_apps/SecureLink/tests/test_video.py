import unittest
from services.video_service import VideoService

class TestVideoService(unittest.TestCase):
    def test_start_video_call(self):
        video_service = VideoService()
        result = video_service.start_video_call(["user1", "user2"])
        self.assertEqual(result, "Video call started successfully")

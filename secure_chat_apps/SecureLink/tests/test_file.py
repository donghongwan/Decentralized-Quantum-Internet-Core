import unittest
from services.file_service import FileService

class TestFileService(unittest.TestCase):
    def test_upload_file(self):
        file_service = FileService()
        result = file_service.upload_file("user1", "testfile.txt")
        self.assertEqual(result, "File uploaded successfully")

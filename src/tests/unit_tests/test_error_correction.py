import unittest
from src.core.error_correction import ErrorCorrection

class TestErrorCorrection(unittest.TestCase):
    def setUp(self):
        self.error_correction = ErrorCorrection()

    def test_hamming_code(self):
        """Test Hamming code for error correction."""
        data = "1011"
        encoded = self.error_correction.hamming_encode(data)
        self.assertEqual(encoded, "1011010")  # Example expected output

    def test_correct_error(self):
        """Test correcting a single-bit error."""
        received = "1011011"  # Introduced error in the last bit
        corrected = self.error_correction.correct(received)
        self.assertEqual(corrected, "1011010")  # Expected corrected output

if __name__ == "__main__":
    unittest.main()

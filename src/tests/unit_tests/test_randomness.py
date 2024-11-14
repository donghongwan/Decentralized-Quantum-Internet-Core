import unittest
from src.core.randomness import Randomness

class TestRandomness(unittest.TestCase):
    def setUp(self):
        self.randomness = Randomness()

    def test_generate_random_bits(self):
        """Test generating random bits."""
        bits = self.randomness.generate_random_bits(10)
        self.assertEqual(len(bits), 10)  # Check if the length is correct
        self.assertTrue(all(bit in [0, 1] for bit in bits))  # Check if all bits are 0 or 1

    def test_randomness_distribution(self):
        """Test the distribution of generated random bits."""
        bits = self.randomness.generate_random_bits(1000)
        count_0 = bits.count(0)
        count_1 = bits.count(1)
        self.assertAlmostEqual(count_0, count_1, delta=100)  # Allow some variance

if __name__ == "__main__":
    unittest.main()

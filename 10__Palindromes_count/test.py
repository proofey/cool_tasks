import unittest
from solution import palindromes_count


class TestPalindromes(unittest.TestCase):
    def test_palindromes_count(self):
        self.assertEqual(palindromes_count(10), 0)
        self.assertEqual(palindromes_count(20), 1)
        self.assertEqual(palindromes_count(101), 10)
        self.assertEqual(palindromes_count(92009), 1009)
        self.assertEqual(palindromes_count(99999), 1089)


if __name__ == "__main__":
    unittest.main()
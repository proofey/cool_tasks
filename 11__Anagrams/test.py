import unittest
from solution import anagrams


class TestAnagrams(unittest.TestCase):
    def test_anagrams(self):
        self.assertEqual(anagrams("listen", "silent"), True)
        self.assertEqual(anagrams("LISTEN", "silent"), True)
        self.assertEqual(anagrams("python", "ruby"), False)
        self.assertEqual(anagrams("New York Times", "monkeys write"), True)
        self.assertEqual(anagrams("snake", "sssnakee"), False)


if __name__ == "__main__":
    unittest.main()
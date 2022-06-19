import unittest
from solution import char_histogram, char_histogram2


class TestCharHistogram(unittest.TestCase):
    def test_char_histogram(self):
        self.assertEqual(char_histogram(""), {})
        self.assertEqual(char_histogram("    "), {' ': 4})
        self.assertEqual(char_histogram("Python!"), {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1})
        self.assertEqual(char_histogram("AAAAaaa!!!"), {'A': 4, 'a': 3, '!': 3})
        self.assertEqual(char_histogram("Some very long string here with different casing"), {
                                                                                                'S': 1,
                                                                                                'o': 2,
                                                                                                'm': 1,
                                                                                                'e': 6,
                                                                                                ' ': 7,
                                                                                                'v': 1,
                                                                                                'r': 4,
                                                                                                'y': 1,
                                                                                                'l': 1,
                                                                                                'n': 4,
                                                                                                'g': 3,
                                                                                                's': 2,
                                                                                                't': 3,
                                                                                                'i': 4,
                                                                                                'h': 2,
                                                                                                'w': 1,
                                                                                                'd': 1,
                                                                                                'f': 2,
                                                                                                'c': 1,
                                                                                                'a': 1
                                                                                            })


    def test_char_histogram2(self):
        self.assertEqual(char_histogram2(""), {})
        self.assertEqual(char_histogram2("    "), {' ': 4})
        self.assertEqual(char_histogram2("Python!"), {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1})
        self.assertEqual(char_histogram2("AAAAaaa!!!"), {'A': 4, 'a': 3, '!': 3})
        self.assertEqual(char_histogram2("Some very long string here with different casing"), {
                                                                                                'S': 1,
                                                                                                'o': 2,
                                                                                                'm': 1,
                                                                                                'e': 6,
                                                                                                ' ': 7,
                                                                                                'v': 1,
                                                                                                'r': 4,
                                                                                                'y': 1,
                                                                                                'l': 1,
                                                                                                'n': 4,
                                                                                                'g': 3,
                                                                                                's': 2,
                                                                                                't': 3,
                                                                                                'i': 4,
                                                                                                'h': 2,
                                                                                                'w': 1,
                                                                                                'd': 1,
                                                                                                'f': 2,
                                                                                                'c': 1,
                                                                                                'a': 1
                                                                                            })


if __name__ == "__main__":
    unittest.main()
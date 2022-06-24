import unittest
from solution import word_counter


class TestWordCounter(unittest.TestCase):
    def test_word_counter_1(self):
        word = "actually"
        matrix = [
            ["i", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z", "o", "y", "m"],
            ["e", "v", "n", "h", "t", "r", "x", "e", "k", "y", "d", "a", "i", "l", "c"],
            ["i", "a", "c", "t", "u", "a", "l", "l", "y", "m", "c", "x", "r", "l", "e"],
            ["m", "v", "c", "n", "p", "u", "a", "m", "n", "t", "l", "u", "e", "a", "a"],
            ["q", "r", "i", "t", "w", "e", "a", "q", "u", "p", "r", "x", "t", "u", "z"],
            ["p", "e", "a", "c", "t", "u", "a", "l", "l", "y", "w", "p", "y", "t", "m"],
            ["o", "y", "h", "t", "r", "e", "l", "u", "f", "p", "q", "n", "z", "c", "s"],
            ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e", "q", "a", "r"]
        ]
        self.assertEqual(word_counter(matrix, word), 4)


    def test_word_counter_2(self):
        word = "madam"
        matrix = [
            ["z", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z"],
            ["e", "v", "m", "h", "t", "r", "x", "e", "k", "y", "m", "a"],
            ["i", "a", "c", "a", "u", "a", "l", "l", "y", "a", "c", "x"],
            ["m", "v", "c", "n", "d", "u", "a", "m", "d", "t", "l", "u"],
            ["q", "t", "i", "t", "w", "a", "a", "a", "u", "p", "r", "x"],
            ["p", "e", "m", "a", "d", "a", "m", "l", "l", "y", "w", "p"],
            ["o", "y", "h", "t", "e", "e", "l", "u", "f", "p", "q", "n"],
            ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e"]
        ]
        self.assertEqual(word_counter(matrix, word), 3)


    def test_word_counter_3(self):
        word = "python"
        matrix = [
        ["r", "u", "b", "y"],
        ["r", "u", "b", "y"],
        ["r", "u", "b", "y"],
        ["r", "u", "b", "y"],
        ]
        self.assertEqual(word_counter(matrix, word), 0)


    def test_word_counter_4(self):
        word = "ana"
        matrix = [
            ["i", "a", "n", "a"],
            ["e", "a", "n", "h"],
            ["i", "n", "n", "v"],
            ["m", "v", "a", "a"],
            ["a", "n", "a", "t"]
        ]
        self.assertEqual(word_counter(matrix, word), 3)



if __name__ == "__main__":
    unittest.main()
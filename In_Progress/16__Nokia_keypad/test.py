import unittest
from solution import message_to_numbers, numbers_to_message


class TestNokiaKeypad(unittest.TestCase):
    def test_message_to_numbers(self):
        self.assertEqual(message_to_numbers("abc"), [2, -1, 2, 2, -1, 2, 2, 2])
        self.assertEqual(message_to_numbers("a"), [2])
        self.assertEqual(message_to_numbers("Ivo e Panda"),
                        [1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2])
        self.assertEqual(message_to_numbers("aabbcc"), 
                        [2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2])


    def test_number_to_message(self):
        self.assertEqual(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]), "abc")
        self.assertEqual(numbers_to_message([2, 2, 2, 2]), "a")
        self.assertEqual(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]),
                                                                                                          "Ivo e Panda")


if __name__ == "__main__":
    unittest.main()
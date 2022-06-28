import unittest
from solution import group


class TestGroup(unittest.TestCase):
    def test_group(self):
        self.assertEqual(group([1, 1, 1, 2, 3, 1, 1]), [[1, 1, 1], [2], [3], [1, 1]])
        self.assertEqual(group([1, 2, 1, 2, 3, 3]), [[1], [2], [1], [2], [3, 3]])
        self.assertEqual(group([]), [])
        self.assertEqual(group([1]), [[1]])
        self.assertEqual(group([1, 1, 1, 1]), [[1, 1, 1, 1]])



if __name__ == "__main__":
    unittest.main()
import unittest
from solution import increasing_or_decreasing, Monotonicity


class TestIncreasingDecreasing(unittest.TestCase):
    def test_increasing_and_decreasing(self):
        self.assertEqual(increasing_or_decreasing([1, 2, 3, 4, 5]), Monotonicity.INCREASING)
        self.assertEqual(increasing_or_decreasing([5, 6, -10]), Monotonicity.NONE)
        self.assertEqual(increasing_or_decreasing([1, 1, 1, 1]), Monotonicity.NONE)
        self.assertEqual(increasing_or_decreasing([9, 8, 7, 6]), Monotonicity.DECREASING)
        self.assertEqual(increasing_or_decreasing([]), Monotonicity.NONE)
        self.assertEqual(increasing_or_decreasing([1]), Monotonicity.NONE)
        self.assertEqual(increasing_or_decreasing([1, 100]), Monotonicity.INCREASING)
        self.assertEqual(increasing_or_decreasing([1, 100, 100]), Monotonicity.NONE)
        self.assertEqual(increasing_or_decreasing([100, 1]), Monotonicity.DECREASING)
        self.assertEqual(increasing_or_decreasing([100, 1, 1]), Monotonicity.NONE)
        self.assertEqual(increasing_or_decreasing([100, 1, 2]), Monotonicity.NONE)


if __name__ == "__main__":
    unittest.main()
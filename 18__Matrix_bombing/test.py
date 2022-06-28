import unittest
from solution import matrix_bombing_plan


class TestMatrixBombingPlan(unittest.TestCase):
    def test_matrix_bombing_plan(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = {(0, 0): 42,
                    (0, 1): 36,
                    (0, 2): 37,
                    (1, 0): 30,
                    (1, 1): 15,
                    (1, 2): 23,
                    (2, 0): 29,
                    (2, 1): 15,
                    (2, 2): 26}
        self.assertEqual(matrix_bombing_plan(matrix), expected)


if __name__ == "__main__":
    unittest.main()
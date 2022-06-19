import unittest
from solution import goldbach


class TestGoldbach(unittest.TestCase):
    def test_goldbach(self):
        self.assertEqual(goldbach(4), [(2,2)])
        self.assertEqual(goldbach(6), [(3,3)])
        self.assertEqual(goldbach(8), [(3,5)])
        self.assertEqual(goldbach(10), [(3,7), (5,5)])
        self.assertEqual(goldbach(100),
                        [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)])
        self.assertEqual(goldbach(5), None)


if __name__ == "__main__":
    unittest.main()
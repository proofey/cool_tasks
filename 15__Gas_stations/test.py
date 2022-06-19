import unittest
from solution import gas_stations


class TestGasStations(unittest.TestCase):
    def test_gas_stations(self):
        self.assertEqual(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]),
                                                        [80, 140, 220, 290])
        self.assertEqual(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]),
                                                        [70, 140, 210, 280, 350])
        self.assertEqual(gas_stations(100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150]),
                                                                                [40, 80])
        self.assertEqual(gas_stations(100, 50, [10, 90]), [])


if __name__ == "__main__":
    unittest.main()
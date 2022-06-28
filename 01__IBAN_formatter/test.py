import unittest
from solution import iban_formatter


class TestIbanFormatter(unittest.TestCase):
    def test_iban_formatter(self):
        self.assertEqual(iban_formatter("BG80BNBG96611020345678"), "BG80 BNBG 9661 1020 3456 78")
        self.assertEqual(iban_formatter("BG80 BNBG 9661 1020 3456 78"), "BG80 BNBG 9661 1020 3456 78")
        self.assertEqual(iban_formatter("BG14TTBB94005362446381"), "BG14 TTBB 9400 5362 4463 81")
        self.assertEqual(iban_formatter("BG91UNCR70001864961754"), "BG91 UNCR 7000 1864 9617 54")

if __name__ == "__main__":
    unittest.main()
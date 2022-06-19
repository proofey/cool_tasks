import unittest
from solution import is_credit_card_valid


class TestCreditCard(unittest.TestCase):
    def test_is_credit_card_valid(self):
        self.assertEqual(is_credit_card_valid(79927398713), True)
        self.assertEqual(is_credit_card_valid(79927398715), False)
        self.assertEqual(is_credit_card_valid(4417123456789113), True)


if __name__ == "__main__":
    unittest.main()
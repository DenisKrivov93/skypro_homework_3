import unittest

from src.masks import account_mask, card_mask


class TestMaskingFunctions(unittest.TestCase):

    def test_account_mask(self):
        self.assertEqual(account_mask(1234567890), "**7890")
        self.assertEqual(account_mask("9876543210"), "**3210")

    def test_card_mask(self):
        self.assertEqual(card_mask(1234567812345678), "1234 56** **** 5678")
        self.assertEqual(card_mask("9876543210987654"), "9876 54** **** 7654")

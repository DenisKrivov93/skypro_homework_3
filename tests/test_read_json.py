import unittest
from unittest.mock import patch, mock_open
from utils.read_json import read_transactions_from_json


class TestReadTransactionsFromJson(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='{"transaction_id": 1}')
    def test_read_transactions_with_valid_json(self, mock_file):
        transactions = read_transactions_from_json("test.json")
        self.assertEqual(transactions, [])

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_read_transactions_with_file_not_found(self, mock_file):
        transactions = read_transactions_from_json("test.json")
        self.assertEqual(transactions, [])

    @patch('builtins.open', new_callable=mock_open, read_data='invalid_json_data')
    def test_read_transactions_with_invalid_json(self, mock_file):
        transactions = read_transactions_from_json("test.json")
        self.assertEqual(transactions, [])

import unittest
from unittest.mock import patch

from src.transaction_sum_rub import transaction_sum_rub


class TestTransactionSumRub(unittest.TestCase):
    @patch("src.transaction_sum_rub.ruble_exchange")
    def test_transaction_sum_rub_usd(self, mock_ruble_exchange):
        # Устанавливаем возвращаемое значение для моковой функции ruble_exchange
        mock_ruble_exchange.return_value = 7500.0

        # Создаем моковую транзакцию в USD
        transaction_usd = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

        # Проверяем конвертацию из USD в RUB
        result = transaction_sum_rub(transaction_usd)
        self.assertEqual(result, 7500.0)
        mock_ruble_exchange.assert_called_once_with(100.0, "USD", "RUB")

    @patch("src.transaction_sum_rub.ruble_exchange")
    def test_transaction_sum_rub_eur(self, mock_ruble_exchange):
        # Устанавливаем возвращаемое значение для моковой функции ruble_exchange
        mock_ruble_exchange.return_value = 8800.0

        # Создаем моковую транзакцию в EUR
        transaction_eur = {"operationAmount": {"amount": "100", "currency": {"code": "EUR"}}}

        # Проверяем конвертацию из EUR в RUB
        result = transaction_sum_rub(transaction_eur)
        self.assertEqual(result, 8800.0)
        mock_ruble_exchange.assert_called_once_with(100.0, "EUR", "RUB")

    def test_transaction_sum_rub_rub(self):
        # Создаем моковую транзакцию в RUB
        transaction_rub = {"operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}

        # Проверяем, что сумма в RUB не конвертируется
        result = transaction_sum_rub(transaction_rub)
        self.assertEqual(result, 100.0)

import json
import os
import unittest
from unittest.mock import MagicMock, patch

from dotenv import load_dotenv

from src.external_api import ruble_exchange

load_dotenv()

API_KEY = os.getenv("API_KEY")


class TestRubleExchange(unittest.TestCase):
    @patch("utils.external_api.requests.request")
    def test_ruble_exchange(self, mock_request):
        api_response = {"query": {"amount": 7500.0}}
        mock_request.return_value = MagicMock(text=json.dumps(api_response))

        # Проверяем функцию ruble_exchange для конвертации USD в RUB
        result = ruble_exchange(100.0, "USD", "RUB")
        self.assertEqual(result, 7500.0)

        # Проверяем, что был сделан запрос к правильному URL
        expected_url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100.0"
        mock_request.assert_called_once_with("GET", expected_url, headers={"apikey": f"{API_KEY}"}, data={})

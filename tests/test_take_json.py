import unittest
from unittest.mock import patch, Mock
from utils.take_json import get_json_from_url


class TestGetJsonFromUrl(unittest.TestCase):
    @patch('your_module.requests.get')
    def test_get_json_from_url_success(self, mock_get):
        # Настройка Mock-объекта для успешного ответа
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'key': 'value'}
        mock_get.return_value = mock_response

        url = "http://api.example.com/data"
        result = get_json_from_url(url)

        # Проверки
        mock_get.assert_called_once_with(url)
        self.assertEqual(result, {'key': 'value'})

    @patch('your_module.requests.get')
    def test_get_json_from_url_http_error(self, mock_get):
        # Настройка Mock-объекта для ответа с ошибкой HTTP
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_get.return_value = mock_response

        url = "http://api.example.com/data"
        result = get_json_from_url(url)

        # Проверки
        mock_get.assert_called_once_with(url)
        self.assertIsNone(result)

    @patch('your_module.requests.get')
    def test_get_json_from_url_request_exception(self, mock_get):
        # Настройка Mock-объекта для исключения RequestException
        mock_get.side_effect = requests.exceptions.RequestException

        url = "http://api.example.com/data"
        result = get_json_from_url(url)

        # Проверки
        mock_get.assert_called_once_with(url)
        self.assertIsNone(result)

import requests


def get_json_from_url(url):
    """
    Делает GET-запрос к указанному URL и возвращает JSON-ответ.

    :param url: URL для запроса
    :return: Данные в формате JSON или None в случае ошибки
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверить наличие ошибок HTTP
        return response.json()  # Вернуть JSON-ответ
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None


# Пример использования:
url = "https://www.cbr-xml-daily.ru/daily_json.js"
json_data = get_json_from_url(url)
if json_data is not None:
    print(type(json_data))

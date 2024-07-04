import json


def read_transactions_from_json(file_path):
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            if not isinstance(data, list):
                return []
            return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

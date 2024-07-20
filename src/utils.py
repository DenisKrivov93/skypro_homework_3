import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    filemode="w",
    filename="../logs/utils.log",
)


def read_transactions_from_json(file_path):
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        logging.info(f"Попытка открыть файл: {file_path}")
        with open(file_path, "r") as file:
            data = json.load(file)
            logging.info("Файл успешно прочитан.")

            if not isinstance(data, list):
                logging.warning("Данные не являются списком. Возвращается пустой список.")
                return []

            return data
    except FileNotFoundError:
        logging.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        logging.error(f"Ошибка декодирования JSON в файле: {file_path}")
        return []

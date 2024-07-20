import logging
from typing import Union

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    filemode="w",
    filename="../logs/mask.log",
)


def account_mask(number: Union[int, str]) -> str:
    """Функция принимает номер счета числом и возвращает его с маской"""

    logging.info(f"Вызвана функция account_mask с номером: {number}")

    # Преобразуем входящее число в строку
    new_num = str(number)

    # Проверка длины номера
    if len(new_num) < 4:
        logging.warning("Длина номера меньше 4. Вернётся исходный номер без изменений.")
        return new_num  # Если номер счёта недостаточно длинный, возвращаем его без маски

    # Возвращаем маскированный номер
    masked_number = "**" + new_num[-4:]
    logging.info(f"Возвращаем маскированный номер: {masked_number}")

    return masked_number


def card_mask(number: Union[int, str]) -> str:
    """Функция принимает номер карты числом и возвращает её с маской"""

    logging.info(f"Вызвана функция card_mask с номером: {number}")

    # Преобразуем входящее число в строку
    new_num = str(number)

    # Проверка на длину номера карты
    if len(new_num) < 16:
        logging.warning("Длина номера карты меньше 16. Вернётся исходный номер без изменений.")
        return new_num  # Если номер карты недостаточно длинный, возвращаем его без маски

    # Формируем маскированный номер карты
    masked_number = new_num[:4] + " " + new_num[4:6] + "** **** " + new_num[-4:]
    logging.info(f"Возвращаем маскированный номер карты: {masked_number}")

    return masked_number


print(account_mask(1234567890))

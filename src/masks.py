from typing import Union


def account_mask(number: Union[int, str]) -> str:
    """Функция принимает номер счета числом и возвращает его с маской"""
    new_num = str(number)
    return "**" + new_num[-4:]


def card_mask(number: Union[int, str]) -> str:
    """Функция принимает номер карты числом и возвращает её с маской"""
    new_num = str(number)
    return new_num[:4] + " " + new_num[4:6] + "** **** " + new_num[-4:]

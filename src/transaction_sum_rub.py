from src.external_api import ruble_exchange


def transaction_sum_rub(transaction) -> float:
    """Возвращает сумму по транзакции и конвертирует её в рубли, если указана иная валюта"""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "USD":
        amount_rubles = ruble_exchange(amount, "USD", "RUB")
        return amount_rubles
    elif currency == "EUR":
        amount_rubles = ruble_exchange(amount, "EUR", "RUB")
        return amount_rubles
    elif currency == "RUB":
        amount_rubles = amount
        return amount_rubles

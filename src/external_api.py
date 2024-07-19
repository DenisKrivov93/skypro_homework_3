import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def ruble_exchange(amount: float, from_currency: str, to_currency: str):
    """Получает данные для конвертации и возвращает сумму в рублях обращаясь к API за актуальным курсом"""

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"

    payload = {}
    headers = {"apikey": f"{API_KEY}"}

    response = requests.request("GET", url, headers=headers, data=payload)

    result = response.text
    total_sum = json.loads(result)
    return total_sum["query"]["amount"]

import requests
from .api import api_url
from decouple import config

API_KEY = config("API_KEY")


def get_exchange_rates(pair):
    params = {
        "get": "rates",
        "pairs": pair,
        "key": API_KEY
    }
    try:
        response = requests.get(api_url, params=params)
    except Exception as err:
        print(err)
        return
    data = response.json()
    rate = data.get(pair, None)
    return rate


def convert(amount_of_money, rate):
    if rate:
        return amount_of_money * rate
    return None


def get_result(from_currency, to_currency, amount_of_money):
    pair = from_currency + to_currency
    rate = get_exchange_rates(pair)
    return convert(amount_of_money, rate)



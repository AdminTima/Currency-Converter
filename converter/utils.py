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
    json_resp = response.json()
    data = json_resp.get("data", None)
    rate = data.get(pair)
    return rate


def convert(amount_of_money, rate):
    if rate:
        result = float(amount_of_money) * float(rate)
    else:
        result = None
    return result


def get_result(from_currency, to_currency, amount_of_money):
    pair = from_currency + to_currency
    print(pair)
    rate = get_exchange_rates(pair)
    print(rate)
    return convert(amount_of_money, rate)



import requests
from config import REQUEST_TIMEOUT

BASE_URL = "https://api.coingecko.com/api/v3"


def get_coin_data(coin_id):
    url = f"{BASE_URL}/coins/{coin_id}"

    params = {
        "localization": "false",
        "tickers": "false",
        "market_data": "true",
        "community_data": "false",
        "developer_data": "false",
        "sparkline": "false"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=REQUEST_TIMEOUT
        )

        if response.status_code == 200:
            return response.json()

        return None

    except Exception as e:
        print(e)
        return None


def get_top_coins(limit=250):
    url = f"{BASE_URL}/coins/markets"

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": False
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=REQUEST_TIMEOUT
        )

        if response.status_code == 200:
            return response.json()

        return []

    except Exception as e:
        print(e)
        return []
    TEST_VARIABLE = "WAQAS_TEST"
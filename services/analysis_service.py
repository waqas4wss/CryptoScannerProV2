from api.coingecko import get_coin_data


def analyze_token(coin_id):

    data = get_coin_data(coin_id)

    if not data:
        return None

    market = data["market_data"]

    return {

        "name": data["name"],

        "symbol": data["symbol"].upper(),

        "price": market["current_price"]["usd"],

        "market_cap": market["market_cap"]["usd"],

        "volume": market["total_volume"]["usd"],

        "circulating": market["circulating_supply"],

        "fdv": market["fully_diluted_valuation"]["usd"]
        if market["fully_diluted_valuation"]["usd"]
        else 0

    }
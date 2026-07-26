import api.coingecko as cg


def scan_market():

    coins = cg.get_top_coins()

    result = []

    for coin in coins:

        market_cap = coin["market_cap"]
        volume = coin["total_volume"]

        if market_cap == 0:
            continue

        ratio = volume / market_cap

        if (
            market_cap < 500_000_000
            and volume > 5_000_000
            and ratio > 0.20
        ):

            result.append({

                "Name": coin["name"],

                "Symbol": coin["symbol"].upper(),

                "Price": coin["current_price"],

                "Market Cap": market_cap,

                "Volume": volume,

                "Volume/MCap": round(ratio, 2)

            })

    return result
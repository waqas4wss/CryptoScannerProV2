import api.coingecko as cg


def scan_market():
    print("Loaded from:", cg.__file__)
    print("Functions:", dir(cg))

    coins = cg.get_top_coins()

    return coins[:5]
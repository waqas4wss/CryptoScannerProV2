def calculate_pump_score(market_cap, volume, circulating):

    score = 0

    if market_cap < 100_000_000:
        score += 35

    elif market_cap < 500_000_000:
        score += 25

    elif market_cap < 1_000_000_000:
        score += 15

    if volume > 10_000_000:
        score += 30

    elif volume > 5_000_000:
        score += 20

    if circulating > 0:
        score += 35

    return min(score, 100)
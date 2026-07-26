import streamlit as st
import pandas as pd
from api.coingecko import get_top_coins

st.set_page_config(
    page_title="Market Scanner",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 CryptoScannerPro V2")
st.caption("Live Market Scanner")

if st.button("Scan Market", use_container_width=True):

    with st.spinner("Scanning market..."):

        coins = get_top_coins(20)

    if not coins:
        st.error("Unable to load market data.")
        st.stop()

    data = []

    for coin in coins:

        data.append({
            "Coin": coin["name"],
            "Symbol": coin["symbol"].upper(),
            "Price ($)": coin["current_price"],
            "Market Cap ($)": coin["market_cap"],
            "24H Volume ($)": coin["total_volume"],
            "24H Change %": coin["price_change_percentage_24h"]
        })

    df = pd.DataFrame(data)

    st.success(f"{len(df)} Coins Loaded")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
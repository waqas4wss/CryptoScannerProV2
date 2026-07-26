import streamlit as st

from services.analysis_service import analyze_token
from utils.pump_score import calculate_pump_score

st.set_page_config(
    page_title="CryptoScannerPro V2",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 CryptoScannerPro V2")
st.caption("AI Powered Early Pump Detection System")

st.divider()

coin = st.text_input(
    "🔍 Enter Coin ID",
    placeholder="bitcoin"
)

if st.button("Analyze Token", use_container_width=True):

    if coin == "":
        st.warning("Please enter a token.")
        st.stop()

    data = analyze_token(coin)

    if data is None:
        st.error("Token not found.")
        st.stop()

    c1, c2, c3 = st.columns(3)

    c4, c5, c6 = st.columns(3)

    c1.metric(
        "Price",
        f"${data['price']:,.4f}"
    )

    c2.metric(
        "Market Cap",
        f"${data['market_cap']:,.0f}"
    )

    c3.metric(
        "24H Volume",
        f"${data['volume']:,.0f}"
    )

    c4.metric(
        "Circulating Supply",
        f"{data['circulating']:,.0f}"
    )

    c5.metric(
        "FDV",
        f"${data['fdv']:,.0f}"
    )

    pump = calculate_pump_score(
        data["market_cap"],
        data["volume"],
        data["circulating"]
    )

    c6.metric(
        "Pump Score",
        f"{pump}/100"
    )

    st.progress(pump / 100)

    if pump >= 80:
        st.success("🟢 Strong Watchlist")

    elif pump >= 60:
        st.warning("🟡 Watch")

    else:
        st.error("🔴 High Risk")
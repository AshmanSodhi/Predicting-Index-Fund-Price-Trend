import streamlit as st
import requests
import plotly.graph_objs as go
import pandas as pd

# Set up the app layout
st.set_page_config(page_title="Stock Price Prediction", layout="wide")

# Custom CSS for background images and styles
st.markdown("""
<style>
body {
    background-image: url('images/background.jpg');
    background-size: cover;
    color: white;
}
header {
    text-align: center;
}
h2, h3, p {
    color: white;
}
h3 {
    font-family: 'Comic Sans MS', cursive, sans-serif;  /* Example unique font style */
    font-size: 20px;
    font-weight: bold;
    margin-top: 10px;  /* Adjust margin as needed */
}
.logo {
    display: block;
    margin-left: 20px;  /* Adjust margin to shift the logo */
    margin-right: auto;
}
</style>
""", unsafe_allow_html=True)

# Main content section
with st.container():
    # Center the logo and app name using columns
    col1, col2, col3 = st.columns([2, 2, 1])  # Adjust column ratios for alignment
    
    with col1:
        st.write("")
    
    with col2:
        st.image("images/logo.png", width=80, use_column_width=False, caption=None, output_format="auto")
        st.markdown("<h3>WhisperTrader</h3>", unsafe_allow_html=True)
    
    with col3:
        st.write("")
    
    # Header section with welcome message
    st.markdown("""
    <header>
        <h2>📈 Index Fund Price Prediction</h2>
        <p>This app predicts future stock prices using historical data. Choose a stock from the dropdown menu and view the interactive candlestick chart.</p>
    </header>
    """, unsafe_allow_html=True)

    # Dropdown menu for stock selection
    stock_symbol = st.selectbox(
        "Choose a stock symbol",
        ("SPX - S&P 500", "NDX - NASDAQ 100", "RUT - Russell 2000", "DJI - Dow Jones Industrial Average")
    )

    # Map stock symbols to Twelve Data tickers
    stock_map = {
        "SPX - S&P 500": "SPX",
        "NDX - NASDAQ 100": "NDX",
        "RUT - Russell 2000": "RUT",
        "DJI - Dow Jones Industrial Average": "DJI"
    }

    # Basic stock info
    stock_info = {
        "SPX - S&P 500": "The S&P 500 is a stock market index tracking the performance of 500 large companies listed on stock exchanges in the United States.",
        "NDX - NASDAQ 100": "The NASDAQ-100 is a stock market index made up of 100 of the largest non-financial companies listed on the NASDAQ stock exchange.",
        "RUT - Russell 2000": "The Russell 2000 Index is a small-cap stock market index of the smallest 2,000 stocks in the Russell 3000 Index.",
        "DJI - Dow Jones Industrial Average": "The Dow Jones Industrial Average is a stock market index that measures the stock performance of 30 large companies listed on stock exchanges in the United States."
    }

    # Display stock info
    st.subheader(f"About {stock_symbol}")
    st.write(stock_info[stock_symbol])

    # Fetch stock data using Twelve Data API
    api_key = "9f042df999054136af12e837cc98c23c"
    stock_ticker = stock_map[stock_symbol]
    url = f"https://api.twelvedata.com/time_series?symbol={stock_ticker}&interval=1day&outputsize=5000&apikey={api_key}"
    response = requests.get(url).json()
    data = response["values"]

    # Convert data to a DataFrame
    df = pd.DataFrame(data)
    df['datetime'] = pd.to_datetime(df['datetime'])
    df.set_index('datetime', inplace=True)
    df = df.sort_index()

    # Plot the data
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df['open'].astype(float),
        high=df['high'].astype(float),
        low=df['low'].astype(float),
        close=df['close'].astype(float),
        name='market data'
    ))

    fig.update_layout(
        title=f"{stock_symbol} History",
        yaxis_title="Stock Price (USD per Shares)",
        xaxis_rangeslider_visible=True
    )

    st.plotly_chart(fig, use_container_width=True)

    # Embed live HTML file for predictions
    st.subheader(f"Live {stock_symbol} Trend Predictions")
    st.write("Check out the predictions below:")

    live_predictions_html_map = {
        "SPX - S&P 500": "https://cool-marigold-8ed07f.netlify.app/",
        "NDX - NASDAQ 100": "https://bespoke-kitten-217886.netlify.app/",
        "RUT - Russell 2000": "https://storied-beijinho-0761cb.netlify.app/",
        "DJI - Dow Jones Industrial Average": "https://cozy-horse-ee6821.netlify.app/"
    }

    if stock_symbol in live_predictions_html_map:
        html_url = live_predictions_html_map[stock_symbol]
        st.components.v1.iframe(html_url, height=600)
    else:
        st.error("Error: No HTML URL specified for selected stock symbol")

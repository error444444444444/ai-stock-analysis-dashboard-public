import streamlit as st
import yfinance as yf
import pandas_ta as ta
from datetime import date
from openai import OpenAI
import os

st.set_page_config(page_title="AI Stock Dashboard", layout="wide")
st.title("🤖 AI-Powered Stock Analysis Dashboard")

symbol = st.text_input("Enter Stock Symbol (e.g., RELIANCE.NS, AAPL)", "RELIANCE.NS")

if st.button("Analyze"):
    data = yf.download(symbol, period="6mo")
    data["RSI"] = ta.rsi(data["Close"])
    data["EMA"] = ta.ema(data["Close"])
    macd = ta.macd(data["Close"])
    data["MACD"] = macd["MACD_12_26_9"]
    data["Signal"] = macd["MACDs_12_26_9"]

    st.line_chart(data[["Close", "EMA"]])
    st.line_chart(data[["RSI"]])

    latest = data.iloc[-1]
    prompt = f"""
    Stock analysis for {symbol} on {date.today()}:
    - RSI: {latest['RSI']:.2f}
    - EMA: {latest['EMA']:.2f}
    - MACD: {latest['MACD']:.2f}
    - Signal Line: {latest['Signal']:.2f}

    Provide a technical summary in plain English.
    """

    openai_key = os.getenv("OPENAI_API_KEY", "your-api-key")
    client = OpenAI(api_key=openai_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    st.subheader("🧠 AI Summary")
    st.write(response.choices[0].message.content.strip())

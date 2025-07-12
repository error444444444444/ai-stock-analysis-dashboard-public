# 🤖 AI-Powered Stock Analysis Dashboard

This Streamlit-based dashboard combines stock market data with AI-driven analysis to deliver intelligent summaries of technical indicators like RSI, MACD, and EMA. It uses GPT-style models to interpret trends and optionally includes sentiment from recent news headlines.

## 🚀 Features
- 🔎 Input any stock symbol (NSE or US)
- 📈 View chart with RSI, EMA, MACD overlays
- 🧠 Get AI-generated summary of technical indicators
- 📰 Optional news sentiment scoring
- 🧾 Export analysis to text/PDF
- 📤 Optional Telegram alert integration

## 🛠️ Tech Stack
- Streamlit for frontend
- yfinance + pandas_ta for data
- OpenAI (or local LLM) for AI analysis
- BeautifulSoup for optional news scraping

## ⚙️ Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🧪 Example Summary

> **TCS.NS Summary:** RSI is at 48, indicating a neutral zone. MACD has just crossed below the signal line, suggesting bearish momentum. The price is trading near the 50-day EMA, showing consolidation. The overall technical outlook is mildly bearish.

## 📄 License
MIT © 2025 Juheb Mahmud


---
### 🔒 Note
This is a public demo version of the **AI Stock Analysis Dashboard**.
For the full working model or custom integrations, please contact the author.

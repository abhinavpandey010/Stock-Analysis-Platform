import requests
import os
from dotenv import load_dotenv
import time
from app.services.cleanData import clean_data
import pandas as pd
load_dotenv()

API_KEY = os.getenv("ALPHA_API_KEY")

TOP_20_SYMBOLS = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "META",
    "TSLA", "NVDA", "BRK.B", "JPM", "JNJ",
    "V", "PG", "UNH", "HD", "MA",
    "DIS", "BAC", "XOM", "NFLX", "ADBE"
]

final_data = []
    
def fetch_daily_ohlcv(symbol):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY,
        "outputsize": "compact"
    }
    response = requests.get(url,params=params)
    
    time.sleep(12)
    return response.json()

for symbol in TOP_20_SYMBOLS:
    data = fetch_daily_ohlcv(symbol)
    if "Time Series (Daily)" not in data:
      print(f"API error / limit hit for {symbol}")
      continue

    symbol_data = data["Time Series (Daily)"]
    
    if symbol_data is None:
        print(f"No data for {symbol}")
        continue
    else:
        df = clean_data(symbol_data,symbol)
    
    final_data.append(df)

final_df = pd.concat(final_data, ignore_index=True)
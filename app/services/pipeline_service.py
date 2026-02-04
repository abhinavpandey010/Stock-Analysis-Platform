from app.services.alphavantage_service import fetch_daily_ohlcv
from app.services.cleanData import clean_data
from app.services.load_data import insert_ohlcv_dataframe
# from app.utils.incremental import filter_new_rows
import pandas as pd

TOP_20_SYMBOLS = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "META",
    "TSLA", "NVDA", "BRK-B", "JPM", "JNJ",
    "V", "PG", "UNH", "HD", "MA",
    "DIS", "BAC", "XOM", "NFLX", "ADBE"
]
final_data = []
def run_ohlcv_pipeline():
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
    final_df["date"] = final_df["date"].dt.date
    insert_ohlcv_dataframe(final_df)

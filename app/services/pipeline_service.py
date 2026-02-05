from app.services.alphavantage_service import fetch_daily_ohlcv
from app.services.cleanData import clean_data
from app.services.load_data import insert_ohlcv_dataframe
from app.services.filter_rows import keep_only_new_rows
# from app.utils.incremental import filter_new_rows
import pandas as pd

TOP_20_SYMBOLS = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "META",
    "TSLA", "NVDA", "BRK-B", "JPM", "JNJ",
    "V", "PG", "UNH", "HD", "MA",
    "DIS", "BAC", "XOM", "NFLX", "ADBE"
]

def run_ohlcv_pipeline():
    final_data = []
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
        
        df = keep_only_new_rows(df,symbol) 
        final_data.append(df)
        
    if not final_data:
        print("No new data for any symbol")
        return

    final_df = pd.concat(final_data, ignore_index=True)
    final_df["date"] = final_df["date"].dt.date
    
    insert_ohlcv_dataframe(final_df)

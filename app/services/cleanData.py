from datetime import datetime
import pandas as pd


def clean_data(symbol_data,symbol):
        df = pd.DataFrame(symbol_data).T
        df.columns = ["open", "high", "low", "close", "volume"]
        df.index.name = 'date'
        df = df.reset_index()
        df["symbol"] = symbol
        df = df[["date", "symbol", "open", "high", "low", "close", "volume"]]
        
        df['date'] = pd.to_datetime(df['date'])
        df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].apply(pd.to_numeric)
        df = df.sort_values(by="date")
        df = df.drop_duplicates(subset=['date','symbol'], keep='last') 
        df = df.reset_index(drop=True)
        
        return df
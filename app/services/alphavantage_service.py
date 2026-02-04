import requests
import os
from dotenv import load_dotenv
import time
from app.services.cleanData import clean_data
import pandas as pd
load_dotenv()

API_KEY = os.getenv("ALPHA_API_KEY")




    
def fetch_daily_ohlcv(symbol):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY,
        "outputsize": "compact"
    }
    response = requests.get(url,params=params)
    response.raise_for_status()

    time.sleep(12)
    return response.json()



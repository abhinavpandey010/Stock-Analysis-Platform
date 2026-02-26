from sqlalchemy import func
from app.models.ohlcv_model import OHLCV
from app.extensions import db
import pandas as pd

def get_last_saved_date(symbol):
        return (
            db.session.query(func.max(OHLCV.date))
            .filter(OHLCV.symbol == symbol)
            .scalar()
        )  
def keep_only_new_rows(df, symbol):
    last_date = get_last_saved_date(symbol)

    if last_date is None:
        return df  # first run → insert everything
    last_date = pd.to_datetime(last_date)
    return df[df["date"] > last_date]
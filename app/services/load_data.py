from app.extensions import db
from app.models.ohlcv_model import OHLCV

def insert_ohlcv_dataframe(df):
    

    if df.empty:
        print("No new data to insert")
        return

    rows = []

    for _, row in df.iterrows():
        rows.append(
            OHLCV(
                date=row["date"],
                symbol=row["symbol"],
                open=row["open"],
                high=row["high"],
                low=row["low"],
                close=row["close"],
                volume=row["volume"]
            )
        )

    try:
        db.session.bulk_save_objects(rows)
        db.session.commit()
        print(f"Inserted {len(rows)} rows into database")
    except Exception as e:
        db.session.rollback()
        print("Database insert failed:", e)

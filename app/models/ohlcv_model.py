from app.extensions import db

class OHLCV(db.Model):
    
    __tablename__ = "ohlcv_data"
    
    id = db.Column(db.Integer, primary_key = True)
    
    symbol = db.Column(db.String(10), nullable = False, index = True)
    date = db.Column(db.Date, nullable=False, index=True)

    open = db.Column(db.Float, nullable=False)
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    close = db.Column(db.Float, nullable=False)
    volume = db.Column(db.BigInteger, nullable=False)

    __table_args__ = (
        db.UniqueConstraint("symbol", "date", name="uix_symbol_date"),
    )

    def __repr__(self):
        return f"<OHLCV {self.symbol} {self.date}>"
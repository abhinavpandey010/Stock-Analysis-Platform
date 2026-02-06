from flask import Blueprint, request, jsonify
from app.models.ohlcv_model import OHLCV
from app.extensions import db


ohlcv_bp = Blueprint("ohlcv_bp", __name__)

@ohlcv_bp.route("/api/ohlcv", methods=["GET"])
def get_ohlcv_data():
    symbol = request.args.get("symbol")

    if not symbol:
        return jsonify({"error": "symbol is required"}), 400

    data = (
        db.session.query(OHLCV)
        .filter(OHLCV.symbol == symbol.upper())
        .order_by(OHLCV.date)
        .all()
    )

    result = [
        {
            "date": row.date.isoformat(),
            "symbol": row.symbol,
            "open": row.open,
            "high": row.high,
            "low": row.low,
            "close": row.close,
            "volume": row.volume
        }
        for row in data
    ]

    return jsonify(result), 200

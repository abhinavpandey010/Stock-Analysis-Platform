from flask import Blueprint, jsonify
from sqlalchemy import text
from app.extensions import db

test_db_bp = Blueprint("test_db", __name__)

@test_db_bp.route("/db-test", methods=["GET"])
def db_test():
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify({"status": "success", "db": "connected"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

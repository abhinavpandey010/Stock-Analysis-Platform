from flask import Flask
from config import Config
from app.extensions import db

def create_app():
    app  = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.models.ohlcv_model import OHLCV
    
    # test route
    from app.routes.test_db import test_db_bp
    app.register_blueprint(test_db_bp)
    
    from app.routes.home import main
    app.register_blueprint(main)
    
    return app
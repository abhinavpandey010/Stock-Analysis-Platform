from flask import Flask
from config import Config
from app.extensions import db

def create_app():
    app  = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # test route
    from app.routes.test_db.routes import test_db_bp
    app.register_blueprint(test_db_bp)
    
    from app.routes.main.routes import main
    app.register_blueprint(main)
    
    return app
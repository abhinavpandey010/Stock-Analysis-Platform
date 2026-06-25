from app import create_app
from app.services.pipeline_service import run_ohlcv_pipeline

app = create_app()

with app.app_context():
    run_ohlcv_pipeline()

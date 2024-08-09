from flask import Flask
from config import config
from .error_handler import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    register_error_handlers(app)

    return app
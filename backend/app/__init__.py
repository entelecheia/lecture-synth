"""
Flask application factory.

This module contains the create_app function, which is responsible for
initializing and configuring the Flask application. It sets up CORS,
registers blueprints, and adds a health check endpoint.

Returns:
    Flask: The configured Flask application instance.
"""

from flask import Flask
from flask_cors import CORS

from .config import Config
from .routes import routes as routes_blueprint


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize CORS
    CORS(app)

    # Initialize any other extensions here (e.g., database)

    # Register blueprints
    app.register_blueprint(routes_blueprint, url_prefix="/api")

    @app.route("/health")
    def health_check():
        return {"status": "healthy"}, 200

    return app

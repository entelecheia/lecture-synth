"""
Configuration settings for the backend application.

This module loads environment variables and defines configuration
settings for various components of the application, including:
- Flask settings
- API keys
- JWT configuration
- Database configuration (commented out)

The Config class uses environment variables to set values, with
fallback default values where appropriate.

Usage:
    from config import Config
    app.config.from_object(Config)
"""

import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    # Flask
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
    DEBUG = os.getenv("DEBUG", "False") == "True"

    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    # JWT Configuration
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-jwt-secret-key")
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRATION_DELTA = 1  # Token expiration in days

    # Database Configuration (if needed)
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Add any other configuration variables here

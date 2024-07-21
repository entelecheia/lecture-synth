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

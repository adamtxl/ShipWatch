import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Database connection string
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for session management
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_secret_key')

    # Optional: Debug settings
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    ENV = os.getenv('ENV', 'development')
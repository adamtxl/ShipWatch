from flask import Flask
from models import db
from routes import register_routes
from config import Config

# Initialize the Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Register routes
register_routes(app)

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])

    # Add this temporarily to app.py or config.py
print("Database URL:", Config.SQLALCHEMY_DATABASE_URI)
print("Secret Key:", Config.SECRET_KEY)
print("Debug Mode:", Config.DEBUG)
from flask import Flask
from models import db
from flask_migrate import Migrate
from routes import register_routes
from config import Config
from flask_jwt_extended import JWTManager


# Initialize the Flask app
app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)

# Initialize database
db.init_app(app)
migrate = Migrate(app, db)

# Register routes
register_routes(app)

# Define root route
@app.route('/')
def home():
    return "Welcome to ShipWatch! The server is running."

# Only print debug information if this file is the entry point
if __name__ == '__main__':
    print("Database URL:", app.config['SQLALCHEMY_DATABASE_URI'])
    print("Secret Key:", app.config['SECRET_KEY'])
    print("Debug Mode:", app.config['DEBUG'])
    app.run(debug=app.config['DEBUG'])
from flask import Flask
from models import db
from flask_migrate import Migrate
from routes import register_routes
from config import Config
from flask_jwt_extended import JWTManager
from routes.searches import searches_bp


def create_app():
    # Initialize the Flask app
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)
    
    # Register routes
    register_routes(app)
    
    # Define root route
    @app.route('/')
    def home():
        return "Welcome to ShipWatch! The server is running."

    return app


# Only run the app if this file is the entry point
if __name__ == '__main__':
    app = create_app()
    print("Database URL:", app.config['SQLALCHEMY_DATABASE_URI'])
    print("Secret Key:", app.config['SECRET_KEY'])
    print("Debug Mode:", app.config['DEBUG'])
    app.run(debug=app.config['DEBUG'])
from flask import Blueprint

# Define the Blueprint
cruises_bp = Blueprint('cruises', __name__)

# Example route for searching cruises
@cruises_bp.route('/search', methods=['GET'])
def search_cruises():
    # Mock response for now
    return {
        "message": "Cruise search endpoint working!",
        "data": [
            {"destination": "Bahamas", "price": "$500"},
            {"destination": "Alaska", "price": "$1200"},
            {"destination": "Mediterranean", "price": "$900"}
        ]
    }

# Example route for tracking cruises
@cruises_bp.route('/track', methods=['POST'])
def track_cruise():
    return {"message": "Track cruise endpoint working!"}
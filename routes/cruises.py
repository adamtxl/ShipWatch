from flask import Blueprint, request, jsonify

# Define the Blueprint
cruises_bp = Blueprint('cruises', __name__)

# Mock cruise data
mock_cruises = [
    {"name": "Caribbean Escape", "price": "$799", "link": "http://example.com/book-caribbean"},
    {"name": "Alaska Adventure", "price": "$1200", "link": "http://example.com/book-alaska"},
    {"name": "Mediterranean Getaway", "price": "$999", "link": "http://example.com/book-med"}
]

# Route for searching cruises
@cruises_bp.route('/search', methods=['POST'])
def search_cruises():
    # Get search criteria from the request
    data = request.get_json()
    destination = data.get('destination', '').lower() if data else ''

    # Filter mock data based on destination
    filtered_cruises = [cruise for cruise in mock_cruises if destination in cruise['name'].lower()]

    # Return filtered results or all cruises if no filter is applied
    return jsonify({"cruises": filtered_cruises or mock_cruises})
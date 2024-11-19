from flask import Blueprint

# Define the Blueprint
searches_bp = Blueprint('searches', __name__)

# Example route using the Blueprint
@searches_bp.route('/search', methods=['POST'])
def search_cruises():
    return {"message": "Search endpoint working!"}
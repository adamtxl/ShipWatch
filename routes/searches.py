from flask import request, jsonify
from models import db, SavedSearch  # Assuming SavedSearch is your model for storing searches

@searches_bp.route('/search', methods=['POST'])
def search_cruises():
    # Parse input from the user
    data = request.json
    destination = data.get('destination')
    price_min = data.get('price_min')
    price_max = data.get('price_max')

    # Insert the search criteria into the database
    new_search = SavedSearch(
        destination=destination,
        price_min=price_min,
        price_max=price_max
    )
    db.session.add(new_search)
    db.session.commit()

    return jsonify({"message": "Search saved successfully!", "search_id": new_search.search_id})
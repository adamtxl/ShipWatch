from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db
from models.saved_search import SavedSearch
from models.destinations import Destination

# Create Blueprint
searches_bp = Blueprint('searches', __name__)

# Create a new saved search
@searches_bp.route('', methods=['POST'])
@jwt_required()
def create_saved_search():
    data = request.get_json()
    user_id = get_jwt_identity()

    # Extract data
    destination_id = data.get('destination_id')
    price_min = data.get('price_min')
    price_max = data.get('price_max')
    number_of_nights = data.get('number_of_nights')

    # Validate destination
    destination = Destination.query.get(destination_id)
    if not destination:
        return jsonify({"error": "Invalid destination ID"}), 400

    # Create the saved search
    new_search = SavedSearch(
        user_id=user_id,
        destination_id=destination_id,
        price_min=price_min,
        price_max=price_max,
        number_of_nights=number_of_nights
    )
    db.session.add(new_search)
    db.session.commit()

    return jsonify({"message": "Saved search created successfully"}), 201

# Get all saved searches for the logged-in user
@searches_bp.route('', methods=['GET'])
@jwt_required()
def get_saved_searches():
    user_id = get_jwt_identity()
    searches = SavedSearch.query.filter_by(user_id=user_id).all()
    
    result = []
    for search in searches:
        result.append({
            "id": search.id,
            "destination": search.destination.name,
            "price_min": search.price_min,
            "price_max": search.price_max,
            "number_of_nights": search.number_of_nights,
            "created_at": search.created_at
        })

    return jsonify(result), 200

# Update a saved search
@searches_bp.route('/<int:search_id>', methods=['PUT'])
@jwt_required()
def update_saved_search(search_id):
    data = request.get_json()
    user_id = get_jwt_identity()

    # Find the saved search
    saved_search = SavedSearch.query.filter_by(id=search_id, user_id=user_id).first()
    if not saved_search:
        return jsonify({"error": "Saved search not found"}), 404

    # Update fields
    saved_search.price_min = data.get('price_min', saved_search.price_min)
    saved_search.price_max = data.get('price_max', saved_search.price_max)
    saved_search.number_of_nights = data.get('number_of_nights', saved_search.number_of_nights)
    destination_id = data.get('destination_id')
    if destination_id:
        destination = Destination.query.get(destination_id)
        if not destination:
            return jsonify({"error": "Invalid destination ID"}), 400
        saved_search.destination_id = destination_id

    db.session.commit()
    return jsonify({"message": "Saved search updated successfully"}), 200

# Delete a saved search
@searches_bp.route('/<int:search_id>', methods=['DELETE'])
@jwt_required()
def delete_saved_search(search_id):
    user_id = get_jwt_identity()

    # Find the saved search
    saved_search = SavedSearch.query.filter_by(id=search_id, user_id=user_id).first()
    if not saved_search:
        return jsonify({"error": "Saved search not found"}), 404

    db.session.delete(saved_search)
    db.session.commit()
    return jsonify({"message": "Saved search deleted successfully"}), 200
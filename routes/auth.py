from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
from models import db
from models.user import User

# Create the Blueprint
auth_bp = Blueprint('auth', __name__)

# User Registration Route
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Extract and validate data
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    # Check if the user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 400

    # Hash the password
    hashed_password = generate_password_hash(password)

    # Create a new user
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    # Generate JWT token for the new user
    access_token = create_access_token(
        identity=str(new_user.id),  # Pass user.id as the identity
        additional_claims={"username": new_user.username},  # Include additional claims if needed
        expires_delta=timedelta(hours=1)
    )

    return jsonify({
        "message": "User registered successfully",
        "access_token": access_token
    }), 201

# User Login Route
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Extract and validate data
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    # Find the user by email
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Generate JWT token
    access_token = create_access_token(
        identity=str(user.id),  # Pass user.id as the identity
        additional_claims={"username": user.username},  # Add extra claims if needed
        expires_delta=timedelta(hours=1)
    )

    return jsonify({"access_token": access_token, "message": f"Welcome, {user.username}!"}), 200

# Protected Route Example
@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()  # This will return user.id as a string
    return jsonify({"logged_in_as": current_user}), 200
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
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

    return jsonify({"message": "User registered successfully"}), 201

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

    # Simulate generating a session or token (add real token handling later)
    return jsonify({"message": f"Welcome, {user.username}!"}), 200

# User Logout Route (optional, for session-based auth)
@auth_bp.route('/logout', methods=['POST'])
def logout():
    # Placeholder for logout functionality
    return jsonify({"message": "Logged out successfully"}), 200
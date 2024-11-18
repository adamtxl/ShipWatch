from flask import Blueprint

# Create the Blueprint
auth_bp = Blueprint('auth', __name__)

# Example route
@auth_bp.route('/login', methods=['POST'])
def login():
    return {"message": "Login route working!"}
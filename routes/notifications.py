from flask import Blueprint

# Define the Blueprint
notifications_bp = Blueprint('notifications', __name__)

# Example route for testing
@notifications_bp.route('/notifications', methods=['GET'])
def get_notifications():
    return {"message": "Notifications route working!"}
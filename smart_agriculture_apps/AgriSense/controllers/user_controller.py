from flask import Blueprint, request, jsonify
from models.user import User
from services.notification_service import NotificationService

bp = Blueprint('user', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    # Add user to the database
    return jsonify({"message": "User  registered successfully!"}), 201

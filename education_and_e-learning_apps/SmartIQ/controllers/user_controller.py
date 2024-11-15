from flask import Blueprint, request, jsonify
from models import User
from services import NotificationService

bp = Blueprint('user', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    NotificationService.send_email("Welcome to SmartIQ", new_user.email, "Thank you for registering!")
    return jsonify({"message": "User  registered successfully!"}), 201

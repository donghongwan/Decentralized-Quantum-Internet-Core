from flask import Blueprint, request, jsonify
from services.user_service import UserService

bp = Blueprint('user', __name__)

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = UserService.create_user(data['username'], data['email'], data['password'])
    return jsonify({'id': user.id, 'username': user.username}), 201

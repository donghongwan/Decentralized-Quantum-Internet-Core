from flask import Blueprint, request, jsonify
from services.user_service import UserService

bp = Blueprint('user', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    user = UserService.register_user(data['username'], data['email'], data['password'], data['role'])
    return jsonify({"id": user.id}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    token = UserService.authenticate_user(data['username'], data['password'])
    if token:
        return jsonify({"token": token}), 200
    return jsonify({"message": "Invalid credentials"}), 401

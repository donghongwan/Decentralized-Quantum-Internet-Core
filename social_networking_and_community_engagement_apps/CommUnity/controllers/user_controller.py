from flask import Blueprint, request, jsonify
from services.user_service import register_user, authenticate_user

bp = Blueprint('user', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    token = register_user(data['username'], data['email'], data['password'])
    return jsonify(access_token=token), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    token = authenticate_user(data['email'], data['password'])
    if token:
        return jsonify(access_token=token), 200
    return jsonify(message='Invalid credentials'), 401

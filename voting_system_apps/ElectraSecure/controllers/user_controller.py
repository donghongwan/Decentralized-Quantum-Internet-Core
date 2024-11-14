from flask import request, jsonify
from services.user_service import UserService

class UserController:
    def __init__(self, app):
        self.user_service = UserService()
        app.add_url_rule('/register', 'register', self.register, methods=['POST'])
        app.add_url_rule('/login', 'login', self.login, methods=['POST'])

    def register(self):
        data = request.json
        self.user_service.register_user(data['username'], data['password'])
        return jsonify({"message": "User  registered successfully"}), 201

    def login(self):
        data = request.json
        if self.user_service.authenticate_user(data['username'], data['password']):
            return jsonify({"message": "Login successful"}), 200
        return jsonify({"message": "Invalid credentials"}), 401

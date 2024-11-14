from flask import request, jsonify
from services.chat_service import ChatService

class UserController:
    def __init__(self, app):
        self.app = app
        self.chat_service = ChatService()
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/user', methods=['POST'])
        def create_user():
            data = request.json
            # Logic to create a user
            return jsonify({"message": "User created successfully"}), 201

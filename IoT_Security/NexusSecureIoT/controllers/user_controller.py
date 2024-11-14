from flask import request, jsonify
from services.user_service import UserService

class UserController:
    def __init__(self, app):
        self.user_service = UserService()
        app.add_url_rule('/users', 'create_user', self.create_user, methods=['POST'])

    def create_user(self):
        data = request.json
        user = self.user_service.create_user(data)
        return jsonify(user), 201

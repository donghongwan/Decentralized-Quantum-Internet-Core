from flask import request

class UserController:
    def __init__(self, app):
        self.app = app
        self.app.add_url_rule('/user', 'create_user', self.create_user, methods=['POST'])

    def create_user(self):
        data = request.json
        user = User(data['username'], data['email'])
        return {"message": "User  created successfully"}, 201

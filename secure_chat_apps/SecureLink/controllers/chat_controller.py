from flask import request, jsonify
from services.chat_service import ChatService

class ChatController:
    def __init__(self, app):
        self.app = app
        self.chat_service = ChatService()
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/chat/send', methods=['POST'])
        def send_message():
            data = request.json
            self.chat_service.send_message(data['sender'], data['receiver'], data['content'])
            return jsonify({"message": "Message sent successfully"}), 200

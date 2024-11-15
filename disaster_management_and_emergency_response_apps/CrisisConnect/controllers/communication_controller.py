from flask import Blueprint, request, jsonify
from services.communication_service import CommunicationService

bp = Blueprint('communication', __name__)

@bp.route('/messages', methods=['POST'])
def send_message():
    data = request.get_json()
    message = CommunicationService.send_message(data['user_id'], data['message'])
    return jsonify({'id': message.id, 'message': message.message}), 201

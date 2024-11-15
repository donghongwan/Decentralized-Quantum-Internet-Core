from flask import Blueprint, request, jsonify
from services.game_service import GameService

bp = Blueprint('game', __name__)

@bp.route('/session', methods=['POST'])
def create_session():
    data = request.json
    session = GameService.create_game_session(data['user_id'], data['score'], data['duration'])
    return jsonify({'id': session.id}), 201

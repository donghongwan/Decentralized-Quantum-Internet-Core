from flask import Blueprint, request, jsonify
from services.ar_service import ARService

bp = Blueprint('ar', __name__)

@bp.route('/experience', methods=['POST'])
def create_experience():
    data = request.json
    experience = ARService.create_experience(data['title'], data['description'], data['content'])
    return jsonify({'id': experience.id}), 201

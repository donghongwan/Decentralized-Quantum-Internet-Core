from flask import Blueprint, request, jsonify
from services.event_service import create_event

bp = Blueprint('event', __name__)

@bp.route('/events', methods=['POST'])
def create():
    data = request.json
    event = create_event(data['title'], data['description'], data['date'], data['group_id'])
    return jsonify(id=event.id, title=event.title), 201

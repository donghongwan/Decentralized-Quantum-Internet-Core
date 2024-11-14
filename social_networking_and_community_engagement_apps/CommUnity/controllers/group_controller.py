from flask import Blueprint, request, jsonify
from services.group_service import create_group

bp = Blueprint('group', __name__)

@bp.route('/groups', methods=['POST'])
def create():
    data = request.json
    group = create_group(data['name'], data['description'])
    return jsonify(id=group.id, name=group.name), 201

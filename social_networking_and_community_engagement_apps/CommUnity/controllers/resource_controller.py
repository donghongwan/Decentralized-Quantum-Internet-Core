from flask import Blueprint, request, jsonify
from services.resource_service import share_resource

bp = Blueprint('resource', __name__)

@bp.route('/resources', methods=['POST'])
def share():
    data = request.json
    resource = share_resource(data['title'], data['description'], data['owner_id'])
    return jsonify(id=resource.id, title=resource.title), 201

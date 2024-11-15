from flask import Blueprint, request, jsonify
from services.resource_service import ResourceService

bp = Blueprint('resource', __name__)

@bp.route('/resources', methods=['POST'])
def add_resource():
    data = request.get_json()
    resource = ResourceService.add_resource(data['type'], data['quantity'], data['location'], data['incident_id'])
    return jsonify({'id': resource.id, 'type': resource.type}), 201

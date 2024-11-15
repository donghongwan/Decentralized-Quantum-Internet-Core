from flask import Blueprint, request, jsonify
from services.incident_service import IncidentService

bp = Blueprint('incident', __name__)

@bp.route('/incidents', methods=['POST'])
def create_incident():
    data = request.get_json()
    incident = IncidentService.create_incident(data['title'], data['description'], data['location'], data['status'])
    return jsonify({'id': incident.id, 'title': incident.title}), 201

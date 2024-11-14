from flask import Blueprint, request, jsonify
from services.project_service import create_project

bp = Blueprint('project', __name__)

@bp.route('/projects', methods=['POST'])
def create():
    data = request.json
    project = create_project(data['title'], data['description'])
    return jsonify(id=project.id, title=project.title), 201

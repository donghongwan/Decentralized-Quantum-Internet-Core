from flask import Blueprint, request, jsonify
from models import Progress

bp = Blueprint('progress', __name__)

@bp.route('/progress', methods=['POST'])
def update_progress():
    data = request.get_json()
    progress = Progress(user_id=data['user_id'], course_id=data['course_id'], completion_percentage=data['completion_percentage'])
    db.session.add(progress)
    db.session.commit()
    return jsonify({"message": "Progress updated successfully!"}), 201

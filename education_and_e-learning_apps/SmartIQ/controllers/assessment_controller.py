from flask import Blueprint, request, jsonify
from services import CourseService

bp = Blueprint('course', __name__)

@bp.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    course = CourseService.create_course(data['title'], data['description'], data['content'])
    return jsonify({"message": "Course created successfully!", "course_id": course.id}), 201

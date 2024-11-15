from flask import Blueprint, jsonify
from services.crop_service import CropService

bp = Blueprint('crop', __name__)

@bp.route('/crop/<int:crop_id>/health', methods=['GET'])
def crop_health(crop_id):
    health_status = CropService.get_crop_health(crop_id)
    return jsonify({"health_status": health_status}), 200

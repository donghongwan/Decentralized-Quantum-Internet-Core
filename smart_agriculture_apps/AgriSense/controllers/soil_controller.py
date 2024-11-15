from flask import Blueprint, jsonify
from services.soil_service import SoilService

bp = Blueprint('soil', __name__)

@bp.route('/soil/<int:soil_id>/moisture', methods=['GET'])
def soil_moisture(soil_id):
    moisture_level = SoilService.get_soil_moisture(soil_id)
    return jsonify({"moisture_level": moisture_level}), 200

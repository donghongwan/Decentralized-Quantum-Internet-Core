from flask import Blueprint, request, jsonify
from services.tracking_service import TrackingService

bp = Blueprint('shipment', __name__)

@bp.route('/track/<int:shipment_id>', methods=['GET'])
def track_shipment(shipment_id):
    tracking_info = TrackingService.get_tracking_info(shipment_id)
    if tracking_info:
        return jsonify(tracking_info), 200
    return jsonify({"message": "Tracking information not found"}), 404

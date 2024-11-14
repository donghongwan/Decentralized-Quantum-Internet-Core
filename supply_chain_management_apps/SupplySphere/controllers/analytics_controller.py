from flask import Blueprint, jsonify
from services.analytics_service import AnalyticsService

bp = Blueprint('analytics', __name__)

@bp.route('/analytics', methods=['GET'])
def get_analytics():
    insights = AnalyticsService.analyze_data()
    return jsonify(insights), 200

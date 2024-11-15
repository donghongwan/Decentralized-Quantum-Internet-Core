from flask import Blueprint, jsonify
from services.weather_service import WeatherService

bp = Blueprint('weather', __name__)

@bp.route('/weather/forecast', methods=['GET'])
def weather_forecast():
    forecast = WeatherService.get_weather_forecast()
    return jsonify({"forecast": forecast.forecast}), 200

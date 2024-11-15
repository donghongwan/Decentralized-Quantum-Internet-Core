from models import Weather

class WeatherService:
    @staticmethod
    def get_weather_forecast():
        return Weather.query.order_by(Weather.id.desc()).first()

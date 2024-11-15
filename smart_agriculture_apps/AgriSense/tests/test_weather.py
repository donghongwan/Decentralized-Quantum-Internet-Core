import unittest
from main import app

class WeatherTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_weather_forecast(self):
        response = self.app.get('/weather/forecast')
        self.assertEqual(response.status_code, 200)

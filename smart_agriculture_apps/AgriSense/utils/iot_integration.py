import requests

def fetch_sensor_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    return None

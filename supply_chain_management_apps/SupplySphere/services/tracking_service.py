import requests

class TrackingService:
    @staticmethod
    def get_tracking_info(shipment_id):
        # Call IoT device API to get real-time tracking data
        response = requests.get(f"http://iot-device-api.local/track/{shipment_id}")
        return response.json() if response.status_code == 200 else None

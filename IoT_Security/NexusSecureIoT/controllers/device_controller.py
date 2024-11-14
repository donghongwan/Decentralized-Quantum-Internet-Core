from flask import request, jsonify
from services.device_service import DeviceService

class DeviceController:
    def __init__(self, app):
        self.device_service = DeviceService()
        app.add_url_rule('/devices', 'register_device', self.register_device, methods=['POST'])

    def register_device(self):
        data = request.json
        device = self.device_service.register_device(data)
        return jsonify(device), 201

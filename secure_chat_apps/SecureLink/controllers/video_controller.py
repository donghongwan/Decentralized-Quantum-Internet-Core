from flask import request, jsonify
from services.video_service import VideoService

class VideoController:
    def __init__(self, app):
        self.app = app
        self.video_service = VideoService()
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/video/start', methods=['POST'])
        def start_video_call():
            data = request.json
            self.video_service.start_video_call(data['participants'])
            return jsonify({"message": "Video call started successfully"}), 200

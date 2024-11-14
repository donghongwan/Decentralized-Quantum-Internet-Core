from flask import request

class MentalHealthController:
    def __init__(self, app):
        self.app = app
        self.app.add_url_rule('/mental_health', 'log_mental_health', self.log_mental_health, methods=['POST'])

    def log_mental_health(self):
        data = request.json
        # Logic to log mental health data for the user
        return {"message": "Mental health data logged successfully"}, 201

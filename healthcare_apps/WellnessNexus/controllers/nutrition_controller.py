from flask import request

class NutritionController:
    def __init__(self, app):
        self.app = app
        self.app.add_url_rule('/nutrition', 'log_nutrition', self.log_nutrition, methods=['POST'])

    def log_nutrition(self):
        data = request.json
        # Logic to log nutrition data for the user
        return {"message": "Nutrition data logged successfully"}, 201

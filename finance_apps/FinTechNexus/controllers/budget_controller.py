from flask import request

class BudgetController:
    def __init__(self, app):
        self.app = app
        self.app.add_url_rule('/budget', 'create_budget', self.create_budget, methods=['POST'])

    def create_budget(self):
        data = request.json
        # Logic to create a budget for the user
        return {"message": "Budget created successfully"}, 201

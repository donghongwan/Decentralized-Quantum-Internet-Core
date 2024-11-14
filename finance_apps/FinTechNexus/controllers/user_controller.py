from flask ```python
import request

class TransactionController:
    def __init__(self, app):
        self.app = app
        self.app.add_url_rule('/transaction', 'add_transaction', self.add_transaction, methods=['POST'])

    def add_transaction(self):
        data = request.json
        transaction = Transaction(data['amount'], data['category'], data['date'])
        # Logic to add transaction to the user
        return {"message": "Transaction added successfully"}, 201

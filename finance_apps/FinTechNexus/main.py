from flask import Flask
from controllers.user_controller import UserController
from controllers.transaction_controller import TransactionController
from controllers.budget_controller import BudgetController

app = Flask(__name__)

# Initialize controllers
user_controller = UserController(app)
transaction_controller = TransactionController(app)
budget_controller = BudgetController(app)

if __name__ == "__main__":
    app.run(debug=True)

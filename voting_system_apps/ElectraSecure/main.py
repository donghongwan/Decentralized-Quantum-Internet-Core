from flask import Flask
from controllers.user_controller import UserController
from controllers.voting_controller import VotingController
from controllers.election_controller import ElectionController

app = Flask(__name__)

# Initialize controllers
user_controller = UserController(app)
voting_controller = VotingController(app)
election_controller = ElectionController(app)

if __name__ == "__main__":
    app.run(debug=True)

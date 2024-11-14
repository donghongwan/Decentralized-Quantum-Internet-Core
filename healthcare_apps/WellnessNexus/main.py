from flask import Flask
from controllers.user_controller import UserController
from controllers.fitness_controller import FitnessController
from controllers.nutrition_controller import NutritionController
from controllers.mental_health_controller import MentalHealthController

app = Flask(__name__)

# Initialize controllers
user_controller = UserController(app)
fitness_controller = FitnessController(app)
nutrition_controller = NutritionController(app)
mental_health_controller = MentalHealthController(app)

if __name__ == "__main__":
    app.run(debug=True)

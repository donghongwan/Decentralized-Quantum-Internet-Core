from flask import Flask
from controllers.device_controller import DeviceController
from controllers.user_controller import UserController
from controllers.compliance_controller import ComplianceController

app = Flask(__name__)

# Initialize controllers
device_controller = DeviceController(app)
user_controller = UserController(app)
compliance_controller = ComplianceController(app)

if __name__ == "__main__":
    app.run(debug=True)

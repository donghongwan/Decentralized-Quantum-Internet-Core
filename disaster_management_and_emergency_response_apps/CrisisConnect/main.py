from flask import Flask
from flask_socketio import SocketIO
from models import db
from controllers import user_controller, incident_controller, resource_controller, communication_controller

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crisisconnect.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

socketio = SocketIO(app)

# Register Blueprints
app.register_blueprint(user_controller.bp)
app.register_blueprint(incident_controller.bp)
app.register_blueprint(resource_controller.bp)
app.register_blueprint(communication_controller.bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app)

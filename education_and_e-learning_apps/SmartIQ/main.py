from flask import Flask
from flask_socketio import SocketIO
from models import db
from controllers import user_controller, course_controller, assessment_controller, progress_controller

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smartiq.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

socketio = SocketIO(app)

# Register Blueprints
app.register_blueprint(user_controller.bp)
app.register_blueprint(course_controller.bp)
app.register_blueprint(assessment_controller.bp)
app.register_blueprint(progress_controller.bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app)

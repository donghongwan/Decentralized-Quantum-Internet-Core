from flask import Flask
from controllers.user_controller import UserController
from controllers.chat_controller import ChatController
from controllers.video_controller import VideoController
from controllers.file_controller import FileController

app = Flask(__name__)

# Initialize controllers
user_controller = UserController(app)
chat_controller = ChatController(app)
video_controller = VideoController(app)
file_controller = FileController(app)

if __name__ == "__main__":
    app.run(debug=True)

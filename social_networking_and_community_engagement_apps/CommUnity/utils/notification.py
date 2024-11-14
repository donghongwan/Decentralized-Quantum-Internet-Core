from flask_socketio import emit

def send_notification(event, message):
    emit('notification', {'event': event, 'message': message}, broadcast=True)

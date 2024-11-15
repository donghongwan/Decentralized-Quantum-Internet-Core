from flask_mail import Mail, Message

class NotificationService:
    def __init__(self, app):
        self.mail = Mail(app)

    def send_alert(self, recipient, subject, body):
        msg = Message(subject, recipients=[recipient])
        msg.body = body
        self.mail.send(msg)

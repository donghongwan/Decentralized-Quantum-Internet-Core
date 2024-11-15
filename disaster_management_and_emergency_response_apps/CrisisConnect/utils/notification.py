from flask_mail import Mail, Message

mail = Mail()

def send_notification(email, subject, body):
    msg = Message(subject, recipients=[email])
    msg.body = body
    mail.send(msg)

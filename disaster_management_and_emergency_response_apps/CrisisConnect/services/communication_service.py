from models.communication import Communication
from models import db

class CommunicationService:
    @staticmethod
    def send_message(user_id, message):
        new_message = Communication(user_id=user_id, message=message, timestamp=datetime.utcnow())
        db.session.add(new_message)
        db.session.commit()
        return new_message

    @staticmethod
    def get_messages_by_user(user_id):
        return Communication.query.filter_by(user_id=user_id).all()

from models import User

class UserService:
    @staticmethod
    def register_user(username, email, password):
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def authenticate_user(email, password):
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            return user.create_token()
        return None

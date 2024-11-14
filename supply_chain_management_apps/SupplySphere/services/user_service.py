from models import User, db

class UserService:
    @staticmethod
    def register_user(username, email, password, role):
        new_user = User(username=username, email=email, password=password, role=role)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def authenticate_user(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:  # Use hashed passwords in production
            return user.create_token()
        return None

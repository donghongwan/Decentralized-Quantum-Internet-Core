from models.user import User
from flask_jwt_extended import create_access_token

def register_user(username, email, password):
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return new_user.create_token()

def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        return create_access_token(identity=user.id)
    return None

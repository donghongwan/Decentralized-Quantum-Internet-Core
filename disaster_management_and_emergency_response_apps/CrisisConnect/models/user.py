from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import create_access_token

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def create_token(self):
        return create_access_token(identity=self.id)

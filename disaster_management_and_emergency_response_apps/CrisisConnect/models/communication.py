from models import db

class Communication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    user = db.relationship('User ', backref=db.backref('communications', lazy=True))

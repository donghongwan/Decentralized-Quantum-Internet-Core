from models import db

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    completion_percentage = db.Column(db.Float, nullable=False)

    user = db.relationship('User ', backref='progress')
    course = db.relationship('Course', backref='progress')

from models import db

class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    questions = db.Column(db.Text, nullable=False)
    answers ```python
    = db.Column(db.Text, nullable=False)

    course = db.relationship('Course', backref='assessments')

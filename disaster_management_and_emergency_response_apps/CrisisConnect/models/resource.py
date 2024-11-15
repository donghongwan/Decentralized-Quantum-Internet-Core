from models import db

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    location ```python
    = db.Column(db.String(200), nullable=False)
    incident_id = db.Column(db.Integer, db.ForeignKey('incident.id'), nullable=False)
    incident = db.relationship('Incident', backref=db.backref('resources', lazy=True))

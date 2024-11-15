from models import db

class Crop(db ```python
.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    health_status = db.Column(db.String(50), nullable=False)
    soil_id = db.Column(db.Integer, db.ForeignKey('soil.id'), nullable=False)

    soil = db.relationship('Soil', backref='crops')

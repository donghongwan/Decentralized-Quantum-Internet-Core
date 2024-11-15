from models import db

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop_id = db.Column(db.Integer, db.ForeignKey('crop.id'), nullable=False)
    data_type = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)

from models import db

class Soil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    moisture_level = db.Column(db.Float, nullable=False)
    nutrient_content = db.Column(db.String(100), nullable=False)

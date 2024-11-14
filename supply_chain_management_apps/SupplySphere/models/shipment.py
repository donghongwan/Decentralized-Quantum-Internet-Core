from models import db

class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey(' supplier.id'), nullable=False)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'), nullable=False)
    consumer_id = db.Column(db.Integer, db.ForeignKey('consumer.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)  # e.g., in transit, delivered
    tracking_info = db.Column(db.JSON, nullable=True)  # JSON for IoT tracking data

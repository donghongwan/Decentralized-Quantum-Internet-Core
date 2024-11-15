from models.resource import Resource
from models import db

class ResourceService:
    @staticmethod
    def add_resource(type, quantity, location, incident_id):
        new_resource = Resource(type=type, quantity=quantity, location=location, incident_id=incident_id)
        db.session.add(new_resource)
        db.session.commit()
        return new_resource

    @staticmethod
    def get_resources_by_incident(incident_id):
        return Resource.query.filter_by(incident_id=incident_id).all()

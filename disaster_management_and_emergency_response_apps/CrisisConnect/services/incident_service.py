from models.incident import Incident
from models import db

class IncidentService:
    @staticmethod
    def create_incident(title, description, location, status):
        new_incident = Incident(title=title, description=description, location=location, status=status)
        db.session.add(new_incident)
        db.session.commit()
        return new_incident

    @staticmethod
    def get_incidents():
        return Incident.query.all()

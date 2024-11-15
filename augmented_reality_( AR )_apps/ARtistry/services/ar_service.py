from models import ARExperience

class ARService:
    @staticmethod
    def create_experience(title, description, content):
        experience = ARExperience(title=title, description=description, content=content)
        db.session.add(experience)
        db.session.commit()
        return experience

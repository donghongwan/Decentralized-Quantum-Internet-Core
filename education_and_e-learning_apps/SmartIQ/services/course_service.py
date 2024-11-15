from models import Course

class CourseService:
    @staticmethod
    def create_course(title, description, content):
        new_course = Course(title=title, description=description, content=content)
        db.session.add(new_course)
        db.session.commit()
        return new_course

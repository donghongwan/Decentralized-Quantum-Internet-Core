from models import Assessment

class AssessmentService:
    @staticmethod
    def create_assessment(course_id, questions, answers):
        new_assessment = Assessment(course_id=course_id, questions=questions, answers=answers)
        db.session.add(new_assessment)
        db.session.commit()
        return new_assessment

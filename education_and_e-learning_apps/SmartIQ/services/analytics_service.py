import pandas as pd
from models import Progress

class AnalyticsService:
    @staticmethod
    def get_user_progress(user_id):
        progress_data = Progress.query.filter_by(user_id=user_id).all()
        return pd.DataFrame([(p.course_id, p.completion_percentage) for p in progress_data], columns=['Course ID', 'Completion Percentage'])

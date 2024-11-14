import pandas as pd

class AnalyticsService:
    def analyze_spending(self, user):
        # Logic to analyze user spending habits
        transactions_df = pd.DataFrame(user.transactions)
        return transactions_df.describe()
